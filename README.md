# enterprise-mcp-server — MCP Server with RAG, Employee, and Ticket Tools

## Overview

This project demonstrates how to build a custom **Model Context Protocol (MCP) server** that exposes reusable tools to AI applications.

Instead of an AI agent directly calling Python functions, MCP provides a standardized protocol that allows AI clients to discover and invoke external tools.

In this project, we build an MCP server that exposes four tool categories: calculator utilities, a RAG-powered document search tool (calling the RAG agent from project 02 over HTTP), an employee PTO lookup, and a ticket status lookup.

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

### calculator_add / calculator_multiply

Basic arithmetic tools.

### search_company_documents

Searches enterprise documents using the RAG pipeline from project 02, called over HTTP. Requires an `api_key` parameter, validated against `MCP_API_KEY`.

Example:

Input:

{
"question": "How many days can employees work remotely?",
"api_key": "your-mcp-api-key"
}


Output:

"Employees can work remotely up to three days per week."

### get_employee_leave

Looks up an employee's remaining PTO days from an in-memory store.

Input: `{"employee_name": "John"}`
Output: `"John has 12 PTO days remaining."`

### get_ticket_information

Looks up ticket status, assigned team, and priority from an in-memory store.

Input: `{"ticket_id": "INC-1001"}`
Output: `"INC-1001 status: In Progress. Assigned team: Platform Engineering. Priority: High."`

> **Note:** Authentication is currently only enforced on `search_company_documents`. The employee and ticket tools don't yet call `authenticate()` — see Future Enhancements.

---

## Project Structure

```
04-mcp-server/

├── server.py
├── auth.py
├── client.py
│
├── tools/
│   ├── calculator.py
│   ├── rag_search.py
│   ├── employee.py
│   └── ticket.py
│
├── database/
│   └── employees.py
│
├── tickets/
│   └── tickets.py
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

- Extend authentication to `get_employee_leave` and `get_ticket_information` (currently only `search_company_documents` is protected)
- Replace in-memory employee/ticket data with real data sources
- Add automated tests for tool call handling and auth failures
- Deploy MCP server as a hosted service
- Connect MCP server as a callable tool set for the multi-agent workflow project

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

## Technologies Used
python, uvicorn, fastmcp, pydantic, typing, mcp
