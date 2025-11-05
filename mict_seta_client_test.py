import asyncio
import nest_asyncio
from mcp import ClientSession
# Explicitly use the streamable-http client for stability
from mcp.client.streamable_http import streamablehttp_client
from typing import Dict, Any

# Required for running asyncio.run inside an interactive python session
nest_asyncio.apply()

# --- CONFIGURATION (Must match the server: http://localhost:8080/mcp) ---
MCP_HOST = "localhost"
MCP_PORT = 8080 
MCP_PATH = "/mcp" 
MCP_URL = f"http://{MCP_HOST}:{MCP_PORT}{MCP_PATH}"


async def main():
    """
    Connects to the FastMCP Server using the stable ClientSession/streamablehttp_client pattern
    and executes the SDP_employer_future_job_skill_predict tool.
    """
    print(f"Connecting to FastMCP Server at: {MCP_URL}")

    # Tool arguments for the SDP_employer_future_job_skill_predict tool
    args1: Dict[str, Any] = {
        "employer_detail": {"name": "TechInnovate Ltd", "sector": "ICT"},
        "future_job_name": "AI Ethics Officer",
        "future_job_description": "Monitors and audits algorithmic decision-making for bias.",
        "LLm_comment_suggestion": "The role will require a mix of technical and legal skills.",
        "skill_to_have_description": "Data governance, machine learning fairness, regulatory compliance."
    }

    try:
        # 1. Connect to the server using Streamable HTTP
        async with streamablehttp_client(MCP_URL) as (
            read_stream,
            write_stream,
            get_session_id,
        ):
            # 2. Establish the MCP session
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()
                print("Successfully established MCP Session.")
                print("-" * 50)

                # 3. List available tools (Verification step)
                tools_result = await session.list_tools()
                print("Available tools:")
                for tool in tools_result.tools:
                    print(f"  - {tool.name}: {tool.description}")
                print("-" * 50)
                
                # 4. Call the target tool
                tool_name = "SDP_employer_future_job_skill_predict"
                print(f"Executing Tool: {tool_name}")
                result = await session.call_tool(
                    tool_name, 
                    arguments=args1
                )

                # 5. Process and display the structured content
                structured_data = result.structured_content
                
                print("✅ SUCCESSFUL Tool Call Response:")
                print(f"  Status: {structured_data.get('status')}")
                print(f"  Message: {structured_data.get('message')}")
                print(f"  Document Path: {structured_data.get('document_path')}")
                
    except Exception as e:
        print(f"❌ CRITICAL ERROR during connection or tool call: {e}")

    print("-" * 50)
    print("Testing complete.")


if __name__ == "__main__":
    asyncio.run(main())
