import asyncio
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_ollama import ChatOllama
import re
from Mcp.systemprompts import McpSystemPrompts
import json
from langchain_openai import AzureOpenAI



class McpClient():
    def __init__(self,base_url):
        # model_name="llama3.3:latest"
        # self.model=ChatOllama(model=model_name, base_url=base_url)
        # self.system_message=McpSystemPrompts.ProcessPlan_SystemPrompt

        self.model = AzureOpenAI(
        api_key="EdN1Hb4xKd6FspZyWTaTOfUX7DmgJCTCOBMNWC906TD6ShhqhHowJQQJ99BDACYeBjFXJ3w3AAABACOG2fHo",
        api_version="2025-01-01-preview",  # check your Azure deployment API version
        azure_endpoint="https://excelacom-llm-openai.openai.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2025-01-01-preview",
        model = "gpt-4o"
    )
        self.system_message=McpSystemPrompts.ProcessPlan_SystemPrompt


    def add_mcp_tool_to_server_py(self,tool_content):
        """
        Inserts a new MCP tool into server.py before the main block.
        """
        try:
            file_path="Mcp\mcp_servers\process_plan\server.py"

         # Generate the MCP tool code
            tool_code = f"""
@mcp.tool()
async def {tool_content.tool_name}_agent_tool():
    \"\"\"
    {tool_content.tool_description}
    \"\"\"
    try:
        context = {{
            "process_plan_name":"{tool_content.tool_name}",
            "process_plan_id": "{tool_content.processplan_id}",
            "description": "{tool_content.tool_description}"
        }}
        return context
    except Exception as e:
        return f"An error occurred: {{str(e)}}"
"""
            # Read server.py
            with open(file_path, "r") as f:
                content = f.read()

            # Insert before `if __name__ == "__main__":`
            updated_content = re.sub(
                r'(?=if __name__ == ["\']__main__["\']\s*:)',
                tool_code + "\n",
                content,
                count=1
            )

            # Write back to server.py
            with open(file_path, "w") as f:
                f.write(updated_content)

            return True
        except Exception as e:
            return False
    
        
    async def run_agent(self,user_query,server_params):
        print(server_params)
        server_params=StdioServerParameters(**server_params)
        print(server_params)
        async with stdio_client(server_params) as (read, write):
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
            try:
                print(agent_response)
                content=agent_response['messages'][-1].content
                mcp_response = json.loads(content)

                process_name = mcp_response.get("process_plan_name")

                if process_name:
                    return {
                        "status": "success",
                        "process_plan_name": process_name
                    }

                return {"status": "failed", "process_plan_name": "-"}

            except (json.JSONDecodeError, TypeError, KeyError) as e:
                return {"status": "failed", "process_plan_name": "-"}
                        