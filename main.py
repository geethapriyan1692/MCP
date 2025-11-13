import asyncio
from mcp_client import McpClient




async def run():
    server_params = {
    "command": "python",
    "args": ["mcp_server.py"]
}
    client = McpClient(model_name="llama3.3:latest", base_url="http://prod-llm.excelacomcloud.net:11434", server_params=server_params)
    user_query = "my last sales order was not delivered, can you help?"
    response = await client.run_agent(user_query)
    print("Agent Response:", response)



if __name__ == "__main__":
    asyncio.run(run())
    print("Finished")
