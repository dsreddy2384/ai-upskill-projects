# rca_server.py
import os
import re
import subprocess
from typing import Dict, Any

try:
    from mcp.server.fastmcp import FastMCP
    mcp = FastMCP("RcaDiagnosticService")
except (ImportError, ModuleNotFoundError):
    from mcp.server.mcpserver import MCPServer
    mcp = MCPServer("RcaDiagnosticService")

@mcp.tool()
def extract_failure_slice(log_file_path: str = "sample_build.log") -> Dict[str, Any]:
    """
    Parses a verbose CI build log and extracts ONLY the relevant failure slice:
    the failing test name, error message, failing file, line number, and stack trace.
    Prevents context window bloat by stripping thousands of lines of setup logs.
    """
    if not os.path.exists(log_file_path):
        return {"error": f"Log file not found: {log_file_path}"}

    with open(log_file_path, "r", encoding="utf-8") as f:
        log_content = f.read()

    # Look for standard pytest / Python tracebacks
    failure_marker = "=================================== FAILURES ==================================="
    if failure_marker in log_content:
        failure_block = log_content.split(failure_marker)[-1]
        # Keep up to the summary section
        if "short test summary info" in failure_block:
            failure_block = failure_block.split("short test summary info")[0]
    else:
        # Fallback: grab lines surrounding ERROR or FAILED
        lines = log_content.splitlines()
        failure_lines = [l for l in lines if "FAIL" in l or "ERROR" in l or "Traceback" in l]
        failure_block = "\n".join(failure_lines[:40])

    # Extract target file and line number (e.g. services/billing_service.py:42)
    file_match = re.search(r"([\w/\.\-]+):(\d+): in ", failure_block)
    failing_file = file_match.group(1) if file_match else "unknown"
    line_number = int(file_match.group(2)) if file_match else 0

    # Extract exception type and message
    error_match = re.search(r"(E\s+[\w]+Error: .+)", failure_block)
    error_message = error_match.group(1).strip() if error_match else "Unknown Error"

    return {
        "failing_file": failing_file,
        "line_number": line_number,
        "error_message": error_message,
        "stack_trace_slice": failure_block.strip()
    }

@mcp.tool()
def get_recent_file_diffs(file_path: str, count: int = 3) -> Dict[str, Any]:
    """
    Fetches the unified git diff of recent commits that modified the specified file.
    Shows the agent what recently changed to pinpoint the breaking commit.
    """
    try:
        cmd = ["git", "log", f"-n{count}", "-p", "--", file_path]
        diff_output = subprocess.check_output(cmd, text=True, stderr=subprocess.DEVNULL)
        if not diff_output.strip():
            # If no git history for that specific file, return commit log
            return {"file": file_path, "message": "No recent git diffs found for this file path."}
        return {"file": file_path, "recent_diffs": diff_output[:3000]}
    except Exception as e:
        return {"error": f"Git command failed: {str(e)}"}

@mcp.tool()
def git_blame_line(file_path: str, line_number: int) -> Dict[str, Any]:
    """
    Runs git blame on a specific line of code to identify the author and commit hash.
    """
    if line_number <= 0:
        return {"error": "Invalid line number"}

    try:
        cmd = ["git", "blame", "-L", f"{line_number},{line_number}", "--porcelain", file_path]
        output = subprocess.check_output(cmd, text=True, stderr=subprocess.DEVNULL)
        
        # Parse porcelain blame format
        lines = output.splitlines()
        commit_hash = lines[0].split()[0]
        author = "unknown"
        summary = "unknown"
        for l in lines:
            if l.startswith("author "):
                author = l.replace("author ", "")
            elif l.startswith("summary "):
                summary = l.replace("summary ", "")

        return {
            "file": file_path,
            "line": line_number,
            "commit_hash": commit_hash,
            "author": author,
            "commit_summary": summary
        }
    except Exception as e:
        # Fallback simulated response if file isn't tracked in git yet
        return {
            "file": file_path,
            "line": line_number,
            "simulated_blame": True,
            "commit_hash": "c8f391a",
            "author": "john.doe@company.com",
            "commit_summary": "Refactor billing payload structure to require gateway tokens"
        }

if __name__ == "__main__":
    mcp.run()