# agent.py
import os
import sys
import json
import asyncio
from google import genai
from google.genai import types
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Initialize Gemini Client (picks up GEMINI_API_KEY from environment)
ai_client = genai.Client()
MODEL_ID = "gemini-2.5-flash"

async def main():
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["server.py"]
    )

    print("Connecting to MCP Server...")
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 1. Fetch available tools dynamically from MCP
            tools_response = await session.list_tools()

            # 2. Translate MCP tools into Gemini function declarations
            function_declarations = []
            for tool in tools_response.tools:
                function_declarations.append(
                    types.FunctionDeclaration(
                        name=tool.name,
                        description=tool.description,
                        parameters=tool.inputSchema
                    )
                )

            gemini_tools = [types.Tool(function_declarations=function_declarations)]

            print(f"Connected! Loaded {len(function_declarations)} tools into Gemini.")
            print("Ask anything about your database in natural language (type 'exit' to quit).\n" + "-" * 55)

            # Initialize multi-turn chat session with tools attached
            chat = ai_client.chats.create(
                model=MODEL_ID,
                config=types.GenerateContentConfig(
                    system_instruction="You are a DevOps database assistant. Inspect schemas and execute read-only queries to answer questions accurately.",
                    tools=gemini_tools
                )
            )

            while True:
                user_query = input("\nYou > ").strip()
                if not user_query:
                    continue
                if user_query.lower() in ("exit", "quit"):
                    print("Shutting down agent...")
                    break

                # Send user prompt to Gemini
                print("Gemini thinking...")
                response = chat.send_message(user_query)

                # ReAct Execution Loop: Handle tool calls as long as the model requests them
                while response.function_calls:
                    for call in response.function_calls:
                        tool_name = call.name
                        tool_args = dict(call.args)

                        print(f"-> Agent calling tool: {tool_name}")
                        print(f"   Arguments: {tool_args}")

                        # Execute the tool via our MCP server over stdio
                        mcp_result = await session.call_tool(tool_name, arguments=tool_args)
                        result_text = mcp_result.content[0].text

                        # Format response back to Gemini
                        tool_response_part = types.Part.from_function_response(
                            name=tool_name,
                            response={"result": result_text}
                        )

                        # Send tool output back so Gemini can synthesize or call another tool
                        response = chat.send_message(tool_response_part)

                # Print the final synthesized answer
                print(f"\nAgent > {response.text}")

if __name__ == "__main__":
    asyncio.run(main())