def create_tool_class(agent_name):
    
    """
        Author : Gnana Bharathi S
        Created On : 23/04/2025
        This method is for creating custom_tool.py file
        """
    
    
    """
    tool_class = "from crewai.tools import BaseTool\n"
    tool_class += "from typing import Type\n"
    tool_class += "from pydantic import BaseModel, Field\n"
    tool_class += "import importlib\n\n"
    """

    tool_class = "class {0}Input(BaseModel):\n".format(agent_name)
    tool_class += "\t\"\"\"Input schema for {0}.\"\"\"\n\n".format(agent_name)

    tool_class += "class {0}(BaseTool):\n".format(agent_name)
    tool_class += "\tname: str = \"{0} Tool\"\n".format(agent_name)
    tool_class += "\tdescription: str = (\n"
    tool_class += "\t\t\"Agent gonna execute the code under the file name AgentFunction.py\"\n"
    tool_class += "\t)\n"
    tool_class += "\targs_schema: Type[BaseModel] = {0}Input\n\n".format(agent_name)

    tool_class += "\tdef _run(self) -> str:\n"

    tool_class += "\t\timport AgentFunction\n"
    tool_class += "\t\timportlib.reload(AgentFunction)\n"
    tool_class += "\t\tfrom main import request_dict\n"
    tool_class += "\t\tglobal shared_response\n"
    tool_class += "\t\tresult = AgentFunction.{0}(shared_response.agentOutput, request_dict.get('{1}'))\n".format(agent_name,str(agent_name))
    tool_class += "\t\tshared_response=AgentOutput(agentOutput=result)\n"
    tool_class += "\t\tFinalOutput.finalOutput=result\n"
    tool_class += "\t\treturn shared_response\n"

    file_path = r"E:/agents/tools/custom_tool.py"

    with open(file_path, 'r') as fp:
        lines = len(fp.readlines())
    class_end = lines+5  # Insert after this line number (0-indexed)

    # Read all lines from the file
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Insert tool_class at the desired line (class_end is line number, index is class_end)
    lines.insert(class_end, tool_class + "\n")

    # Write updated content back to the file
    with open(file_path, "w") as file:
        file.writelines(lines)
    """
    with open(file_path, "w") as file:
        file.write(tool_class)
    """