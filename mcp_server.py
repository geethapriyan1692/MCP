from mcp.server.fastmcp import FastMCP



mcp=FastMCP("Agents server")


@mcp.tool()
async def sales_order_agent_tool() -> str:
    """
     call the agent tool to process the sales order related query
    """
    try:
        return "agentSalesOrderCreation"
    except Exception as e:  
        return f"An error occurred: {str(e)}"

@mcp.tool()
async def cpq_sales_order_agent_tool() -> str:
    """
     call the agent tool to process the cpq sales order related query
    """
    try:
        return "cpqSalesOrderAgent"
    except Exception as e:  
        return f"An error occurred: {str(e)}"






if __name__ == "__main__":
    mcp.run(transport="stdio")