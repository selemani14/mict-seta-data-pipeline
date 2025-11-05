# config.py (FINAL CORRECTED VERSION)

import os
import logging
from fastmcp import FastMCP
from dotenv import load_dotenv

# --- I. CONFIGURATION ---
load_dotenv()

# --- Logging Setup ---
# logger and other variables are DEFINED here.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Report Directory Setup ---
REPORT_DIRECTORY = os.getenv("REPORT_DIR", "mict_reports")
if not os.path.exists(REPORT_DIRECTORY):
    os.makedirs(REPORT_DIRECTORY)
    logger.info(f"Created report directory: {REPORT_DIRECTORY}")

# --- FastMCP Configuration ---
MCP_HOST = os.getenv("MCP_HOST", "localhost")
MCP_PORT = int(os.getenv("MCP_PORT", 8080))
MCP_SERVER_NAME = "MICT SETA Data Pipeline"

# Initialize FastMCP
try:
    mcp = FastMCP(MCP_SERVER_NAME)
    logger.info(f"FastMCP initialized with server name: {MCP_SERVER_NAME}")
except Exception as e:
    logger.critical(f"FastMCP initialization failed: {e}")
    mcp = None

# Export all necessary objects
__all__ = [
    "mcp",
    "logger",
    "REPORT_DIRECTORY",
    "MCP_HOST",
    "MCP_PORT",
]
