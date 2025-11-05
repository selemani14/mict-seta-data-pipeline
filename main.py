# main.py (FINAL CORRECTED VERSION)

import logging
from typing import Optional, List, Dict # Keeping List/Dict for compatibility, though unnecessary in 3.12

# FIX: Ensure all imports of local files are absolute
from config import mcp, logger, MCP_HOST, MCP_PORT 
from report_generator import generate_word_report # FIX: No change, but verifying it is absolute


# --- IV. TOOL DEFINITIONS ---
# ... (Tool definitions remain the same)

if mcp:
    # --------------------------------------------------------------------------------
    # 1. Predictive Tools (Future-Looking)
    # --------------------------------------------------------------------------------
    @mcp.tool()
    async def SDP_employer_future_job_skill_predict(employer_detail: dict, future_job_name: str, future_job_description: str, LLm_comment_suggestion: str, skill_to_have_description: str) -> dict:
        """PURPOSE: Identifies a new/emerging job role not yet in the OFO code system. Data forwarded for SDP curriculum planning."""
        params = locals() # Captures all passed arguments as a dictionary
        return await generate_word_report("SDP_employer_future_job_skill_predict", params)

    # ... (all other tool definitions use `dict` and `list` correctly)
    
# --- V. EXECUTION ---
if __name__ == "__main__":
    if mcp:
        logger.info(f"Starting FastMCP Server using Streamable-HTTP transport on {MCP_HOST}:{MCP_PORT}...")
        try:
            mcp.run(transport="streamable-http", host=MCP_HOST, port=MCP_PORT)
        except Exception as e:
             logger.critical(f"CRITICAL UNHANDLED ERROR during server run phase: {e}", exc_info=True)
    else:
        logger.critical("Server initialization failed. Cannot start.") 
