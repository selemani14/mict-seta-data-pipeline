# MICT SETA Data Pipeline (FastMCP Server)

This repository contains a simple server implementation using the `fastmcp` framework, designed to expose data-processing tools related to job skill prediction and curriculum planning for MICT SETA (Media, Information and Communication Technologies Sector Education and Training Authority).

The primary tool, `SDP_employer_future_job_skill_predict`, processes employer data and future job descriptions, and saves the input parameters into a Word document report.
## 🚀 MCP Hackathon Details:

    **Creator Name:** Amundlia Selemani

    **Power Point Presentation Link**: https://slidesmcpchallenge.stentguard.com/mict-seta-data-pipelinePitch.pptx

    **Email:** demuenator@gmail.com
    
## 🚀 Getting Started

### Prerequisites

* Python 3.8+ (The code uses features compatible with modern Python versions, including `asyncio.to_thread`).

### Installation

1.  **Install the dependencies** using the provided `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Server

1.  The server configuration is managed in `config.py` and via environment variables in a `.env` file (not provided, but assumed).
    * **Default Host:** `localhost`
    * **Default Port:** `8080`
    * **Report Directory:** `mict_reports` (created if it doesn't exist)
2.  Start the server by running `main.py`:
    ```bash
    python main.py
    ```
    The server will start and log its host and port.

### Running the Client

The `mict_seta_client_test.py` file demonstrates how to connect to the running server and call the tool.

1.  Ensure the server is running (see above).
2.  Execute the client script:
    ```bash
    python mict_seta_client_test.py
    ```
    The client will:
    * Connect to the server.
    * List available tools for verification.
    * Call the `SDP_employer_future_job_skill_predict` tool with a set of sample arguments.
    * Print the structured response from the server, including the path to the generated report file.

## 📁 Project Structure

* `main.py`: The entry point for the FastMCP server. It initializes the `FastMCP` instance and defines the tools.
* `config.py`: Handles configuration, environment variable loading (`.env`), logging setup, and initializes the `FastMCP` object.
* `report_generator.py`: Contains the logic to generate a `.docx` report from tool parameters. It uses `asyncio.to_thread` to offload synchronous file I/O operations (creation/saving) to a worker thread.
* `mict_seta_client_test.py`: An example client script demonstrating connection to the server and a tool call using `ClientSession` and `streamablehttp_client`.
