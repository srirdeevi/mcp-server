from mcp.server.fastmcp import FastMCP

from tools.calculator import add, multiply
from tools.rag_search import search_documents
from tools.employee import employee_pto
from tools.ticket import ticket_status


mcp = FastMCP(
    "calculator-server"
)


@mcp.tool()
def calculator_add(a: float, b: float) -> float:
    """
    Add two numbers.
    """

    return add(a, b)


@mcp.tool()
def calculator_multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.
    """

    return multiply(a, b)

@mcp.tool()
def search_company_documents(
        question: str,
        api_key: str
):

    return search_documents(
        question,
        api_key
    )

@mcp.tool()
def get_employee_leave(employee_name: str):
    return employee_pto(employee_name)

@mcp.tool()
def get_ticket_information(ticket_id: str):

    return ticket_status(ticket_id)


if __name__ == "__main__":

    print("Starting Calculator MCP Server...")

    mcp.run()
