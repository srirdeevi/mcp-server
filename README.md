# 04-enterprise-mcp-server — MCP Server with RAG Knowledge Tools

## Overview

This project demonstrates how to build a custom **Model Context Protocol (MCP) server** that exposes reusable tools to AI applications.

Instead of an AI agent directly calling Python functions, MCP provides a standardized protocol that allows AI clients to discover and invoke external tools.

In this project, we build a simple MCP server that exposes calculator capabilities.

---

## What is MCP?

**Model Context Protocol (MCP)** is an open protocol that enables AI applications to securely connect with external tools, data sources, and services.

Traditional approach:

```
AI Agent
   |
   v
Direct Python Function Calls
```

enterprise-mcp-server:

```

                MCP Client
                    |
                    |
             Authentication
                    |
                    v
             MCP Server
                    |
     +--------------+--------------+
     |              |              |
     v              v              v

  RAG Tool      Database Tool   API Tool

 search_docs    employee_db    system_health
```

The MCP server acts as a bridge between AI systems and external capabilities.

---

## Architecture

The MCP server exposes enterprise capabilities as AI tools.


```
                 AI Client

                    |
                    |
                    v

              MCP Protocol

                    |
                    v

            Enterprise MCP Server

                    |
                    v

             RAG API Service
                    |
                    v

              Vector Database
                    |
                    v

            Enterprise Documents

```

---

## Features

## Available MCP Tools

### search_company_documents

Searches enterprise documents using a RAG pipeline.

Example:

Input:

{
"question": "How many days can employees work remotely?"
}


Output:

"Employees can work remotely up to three days per week."

---

## Project Structure

```
04-mcp-server/

├── server.py
│
├── tools/
│   └── calculator.py
│
├── README.md
│
└── requirements.txt
```

---

## Technology Stack

- Python 3.11+
- Model Context Protocol (MCP)
- FastMCP
- Python functions exposed as AI tools

---

## Installation

### 1. Clone repository

```bash
git clone <repository-url>
```

Navigate:

```bash
cd 04-mcp-server
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate:

Mac/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the MCP Server

Start the server:

```bash
python server.py
```

The MCP server will start and expose available tools.

---

## Example Tool Definition

Example MCP tool:

```python
@mcp.tool()
def calculator_add(a: float, b: float) -> float:

    return a + b
```

The function becomes discoverable as an MCP tool.

---

## Learning Outcomes

Through this project, I learned:

- How MCP works as a communication layer for AI applications
- How to create custom MCP tools
- How to expose Python functions as AI capabilities
- How AI agents can discover and use external tools
- The difference between traditional function calls and protocol-based tool access

---

## Future Enhancements

Planned improvements:

- Add database MCP tools
- Connect MCP server with an AI agent
- Add RAG-powered knowledge retrieval tool
- Add API integration tools
- Add authentication and authorization
- Deploy MCP server as a service

---

## Relationship to Previous Projects

This project builds on previous AI engineering concepts:

### Project 01 — Basic Tool Use

```
Agent
 |
 +-- Tools
```

### Project 02 — RAG Agent

```
Documents
 |
 v
Vector Database
 |
 v
Knowledge Retrieval
```

### Project 03 — Multi-Agent Workflow

```
Orchestrator
 |
 +-- Research Agent
 +-- Writer Agent
```

### Project 04 — MCP Server

```
AI System
 |
 v
MCP Protocol
 |
 v
Reusable External Tools
```

---

## Author

AI Engineering Portfolio Project
