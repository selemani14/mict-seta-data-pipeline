MICT SETA Data Pipeline (mict-seta-data-pipeline)

🚀 Project Overview

This repository hosts a core component of the MICT SETA Sector Skills Plan (SSP) initiative: a structured Data Pipeline Server.

The server is built using the FastMCP (Model Context Protocol) framework and is designed to act as a structured data collection gateway. It receives predefined, validated data payloads from Large Language Models (LLMs) via 12 dedicated data collection tools and securely forwards them to an external Report Generator API for deep skills analysis and strategic foresight reporting.

Key Features

FastMCP-Based Tooling: Defines 12 specific tools (functions) for granular data collection.

Asynchronous Forwarding: Uses asynchronous HTTP to quickly forward structured data to a downstream API.

Configuration: Uses .env for easy configuration of server host, port, and API endpoint.

Test Client: Includes a simple requests-based client to verify end-to-end communication.

🛠️ Project Structure

File

Description

edu_workflow_mcp_server2.py

The main asynchronous FastMCP server application, containing all 12 data collection tool definitions.

test_client.py

A simple Python script used to test the connection and data flow to one of the server's tools.

project_config.env

Configuration file for server host, port, and the target Report API URL.

requirements.txt

Lists all necessary Python dependencies (fastmcp, python-dotenv, requests, etc.).

README.md

This setup and usage guide.

.gitignore

Ensures development files and sensitive configurations are not committed to Git.

⚙️ Setup and Installation

1. Clone the Repository

Clone the project to your local machine and navigate into the directory:

git clone
