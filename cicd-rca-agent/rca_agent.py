# rca_agent.py
import os
import sys
import asyncio
from google import genai
from google.genai import types
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Initialize Gemini Client (reads GEMINI_API_KEY from environment)
ai_client = genai.Client()
MODEL_ID = "gemini-2.5-flash"

SYSTEM_INSTRUCTION = """
You are an expert CI/CD Root Cause Analysis (RCA) Engineer.
When a build failure occurs, you autonomously investigate by:
1. Slicing the build log to isolate the failing test, file, and line number.
2. Checking git blame and recent diffs for that line and file to identify who modified it and why.
3. Generating a structured, executive RCA report with:
   - Failing Test & Exception
   - Root Cause Diagnosis
   - Culprit Commit & Author
   - Recommended Code Fix (exact diff or patch)
"""

async def run_rca_investigation(log_file: str = "sample_build.log"):
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["rca_server.py"]
    )

    print("==================================================")
    print("🚀 Initializing Autonomous CI/CD RCA Agent...")
    print("==================================================")

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 1. Fetch tools dynamically from MCP
            tools_response = await session.list_tools()
            
            # 2. Convert to Gemini function declarations
# 2. Convert to Gemini function declarations
            function_declarations = [
                types.FunctionDeclaration(
                    name=tool.name,
                    description=tool.description,
                    parameters=getattr(tool, "input_schema", getattr(tool, "inputSchema", {}))
                )
                for tool in tools_response.tools
            ]

            gemini_tools = [types.Tool(function_declarations=function_declarations)]
            print(f"Loaded {len(function_declarations)} diagnostic tools from MCP server.\n")

            # 3. Create chat session
            chat = ai_client.chats.create(
                model=MODEL_ID,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION,
                    tools=gemini_tools
                )
            )

            # 4. Trigger the investigation
            prompt = f"A build failure just occurred in CI. Please investigate '{log_file}', identify what broke, determine who and what commit caused it, and provide a fix."
            print(f"Triggering investigation: '{prompt}'\n")

            response = chat.send_message(prompt)

            # 5. ReAct Execution Loop: Execute tools requested by Gemini
            step_count = 1
            while response.function_calls:
                for call in response.function_calls:
                    tool_name = call.name
                    tool_args = dict(call.args)

                    print(f"[Step {step_count}] Agent executing: {tool_name}")
                    print(f"         Arguments: {tool_args}")

                    # Execute via MCP
                    mcp_result = await session.call_tool(tool_name, arguments=tool_args)
                    result_text = mcp_result.content[0].text

                    # Feed result back to the model
                    tool_response_part = types.Part.from_function_response(
                        name=tool_name,
                        response={"result": result_text}
                    )
                    response = chat.send_message(tool_response_part)
                    step_count += 1

            # 6. Final RCA Report
            print("\n==================================================")
            print("📋 FINAL ROOT CAUSE ANALYSIS (RCA) REPORT")
            print("==================================================")
            print(response.text)

if __name__ == "__main__":
    asyncio.run(run_rca_investigation("sample_build.log"))