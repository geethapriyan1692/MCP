import asyncio
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_ollama import ChatOllama



class McpClient():
    def __init__(self,model_name,base_url,server_params):
        self.model=ChatOllama(model="llama3.3:latest", base_url="http://prod-llm.excelacomcloud.net:11434")
        self.server_params=StdioServerParameters(**server_params)
        self.system_message="You are a helpful assistant that uses tools to answer user queries."




    async def run_agent(self,user_query):
        async with stdio_client(self.server_params) as (read, write):
            async with ClientSession(read, write) as session:
                # Initialize the connection
                await session.initialize()

                # Get tools
                tools = await load_mcp_tools(session)

                # Create and run the agent
                agent = create_react_agent(model=self.model, prompt=self.system_message, tools=tools)
                agent_response = await agent.ainvoke(
                    {
                        "messages": user_query
                    }
                )
                return agent_response
            

