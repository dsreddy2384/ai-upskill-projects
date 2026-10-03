# test_debug.py
print("STEP 1: Starting script...")

from mcp.server.fastmcp import FastMCP
print("STEP 2: FastMCP imported successfully.")

mcp = FastMCP("DebugTest")

@mcp.tool()
def ping() -> str:
    return "pong"

print("STEP 3: Calling mcp.run()...")
mcp.run()
print("STEP 4: mcp.run() exited.")