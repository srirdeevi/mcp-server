from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


server_params = StdioServerParameters(
    command="python",
    args=["server.py"]
)


async def main():

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()


            # result = await session.call_tool(
            #     "search_company_documents",
            #     {
            #         "question":
            #             "How many days can employees work remotely?",
            #         "api_key":
            #             "my-secret-enterprise-key"
            #     }
            # )

            # result = await session.call_tool(
            #     "get_employee_leave",
            #     {
            #         "employee_name": "John"
            #     }
            # )

            result = await session.call_tool(
                "get_ticket_information",
                {
                    "ticket_id": "INC-1001"
                }
            )


            print("Tool result:")
            print(result)


if __name__ == "__main__":

    import asyncio

    asyncio.run(main())
