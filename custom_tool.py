from typing import Type, Any
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
import importlib
from main import FinalOutput
class AgentOutput(BaseModel):
    	agentOutput: Any
shared_response = AgentOutput(agentOutput="")


class Address_Check_AgentInput(BaseModel):
	"""Input schema for Address_Check_Agent."""

class Address_Check_Agent(BaseTool):
	name: str = "Address_Check_Agent Tool"
	description: str = (
		"Agent gonna execute the code under the file name AgentFunction.py"
	)
	args_schema: Type[BaseModel] = Address_Check_AgentInput

	def _run(self) -> str:
		import AgentFunction
		importlib.reload(AgentFunction)
		from main import request_dict
		global shared_response
		result = AgentFunction.Address_Check_Agent(shared_response.agentOutput, request_dict.get('Address_Check_Agent'))
		shared_response=AgentOutput(agentOutput=result)
		FinalOutput.finalOutput=result
		return shared_response

class AddressValidation_AgentInput(BaseModel):
	"""Input schema for AddressValidation_Agent."""

class AddressValidation_Agent(BaseTool):
	name: str = "AddressValidation_Agent Tool"
	description: str = (
		"Agent gonna execute the code under the file name AgentFunction.py"
	)
	args_schema: Type[BaseModel] = AddressValidation_AgentInput

	def _run(self) -> str:
		import AgentFunction
		importlib.reload(AgentFunction)
		from main import request_dict
		global shared_response
		result = AgentFunction.AddressValidation_Agent(shared_response.agentOutput, request_dict.get('AddressValidation_Agent'))
		shared_response=AgentOutput(agentOutput=result)
		FinalOutput.finalOutput=result
		return shared_response

class Contract_Approval_AgentInput(BaseModel):
	"""Input schema for Contract_Approval_Agent."""

class Contract_Approval_Agent(BaseTool):
	name: str = "Contract_Approval_Agent Tool"
	description: str = (
		"Agent gonna execute the code under the file name AgentFunction.py"
	)
	args_schema: Type[BaseModel] = Contract_Approval_AgentInput

	def _run(self) -> str:
		import AgentFunction
		importlib.reload(AgentFunction)
		from main import request_dict
		global shared_response
		result = AgentFunction.Contract_Approval_Agent(shared_response.agentOutput, request_dict.get('Contract_Approval_Agent'))
		shared_response=AgentOutput(agentOutput=result)
		FinalOutput.finalOutput=result
		return shared_response

class Create_Market_Offering_AgentInput(BaseModel):
	"""Input schema for Create_Market_Offering_Agent."""

class Create_Market_Offering_Agent(BaseTool):
	name: str = "Create_Market_Offering_Agent Tool"
	description: str = (
		"Agent gonna execute the code under the file name AgentFunction.py"
	)
	args_schema: Type[BaseModel] = Create_Market_Offering_AgentInput

	def _run(self) -> str:
		import AgentFunction
		importlib.reload(AgentFunction)
		from main import request_dict
		global shared_response
		result = AgentFunction.Create_Market_Offering_Agent(shared_response.agentOutput, request_dict.get('Create_Market_Offering_Agent'))
		shared_response=AgentOutput(agentOutput=result)
		FinalOutput.finalOutput=result
		return shared_response

class Credit_Check_AgentInput(BaseModel):
	"""Input schema for Credit_Check_Agent."""

class Credit_Check_Agent(BaseTool):
	name: str = "Credit_Check_Agent Tool"
	description: str = (
		"Agent gonna execute the code under the file name AgentFunction.py"
	)
	args_schema: Type[BaseModel] = Credit_Check_AgentInput

	def _run(self) -> str:
		import AgentFunction
		importlib.reload(AgentFunction)
		from main import request_dict
		global shared_response
		result = AgentFunction.Credit_Check_Agent(shared_response.agentOutput, request_dict.get('Credit_Check_Agent'))
		shared_response=AgentOutput(agentOutput=result)
		FinalOutput.finalOutput=result
		return shared_response

class Customer_Profile_Check_AgentInput(BaseModel):
	"""Input schema for Customer_Profile_Check_Agent."""

class Customer_Profile_Check_Agent(BaseTool):
	name: str = "Customer_Profile_Check_Agent Tool"
	description: str = (
		"Agent gonna execute the code under the file name AgentFunction.py"
	)
	args_schema: Type[BaseModel] = Customer_Profile_Check_AgentInput

	def _run(self) -> str:
		import AgentFunction
		importlib.reload(AgentFunction)
		from main import request_dict
		global shared_response
		result = AgentFunction.Customer_Profile_Check_Agent(shared_response.agentOutput, request_dict.get('Customer_Profile_Check_Agent'))
		shared_response=AgentOutput(agentOutput=result)
		FinalOutput.finalOutput=result
		return shared_response

class ID_Fetching_AgentInput(BaseModel):
	"""Input schema for ID_Fetching_Agent."""

class ID_Fetching_Agent(BaseTool):
	name: str = "ID_Fetching_Agent Tool"
	description: str = (
		"Agent gonna execute the code under the file name AgentFunction.py"
	)
	args_schema: Type[BaseModel] = ID_Fetching_AgentInput

	def _run(self) -> str:
		import AgentFunction
		importlib.reload(AgentFunction)
		from main import request_dict
		global shared_response
		result = AgentFunction.ID_Fetching_Agent(shared_response.agentOutput, request_dict.get('ID_Fetching_Agent'))
		shared_response=AgentOutput(agentOutput=result)
		FinalOutput.finalOutput=result
		return shared_response

class Market_Offering_Suggestion_AgentInput(BaseModel):
	"""Input schema for Market_Offering_Suggestion_Agent."""

class Market_Offering_Suggestion_Agent(BaseTool):
	name: str = "Market_Offering_Suggestion_Agent Tool"
	description: str = (
		"Agent gonna execute the code under the file name AgentFunction.py"
	)
	args_schema: Type[BaseModel] = Market_Offering_Suggestion_AgentInput

	def _run(self) -> str:
		import AgentFunction
		importlib.reload(AgentFunction)
		from main import request_dict
		global shared_response
		result = AgentFunction.Market_Offering_Suggestion_Agent(shared_response.agentOutput, request_dict.get('Market_Offering_Suggestion_Agent'))
		shared_response=AgentOutput(agentOutput=result)
		FinalOutput.finalOutput=result
		return shared_response

class Price_Plan_AgentInput(BaseModel):
	"""Input schema for Price_Plan_Agent."""

class Price_Plan_Agent(BaseTool):
	name: str = "Price_Plan_Agent Tool"
	description: str = (
		"Agent gonna execute the code under the file name AgentFunction.py"
	)
	args_schema: Type[BaseModel] = Price_Plan_AgentInput

	def _run(self) -> str:
		import AgentFunction
		importlib.reload(AgentFunction)
		from main import request_dict
		global shared_response
		result = AgentFunction.Price_Plan_Agent(shared_response.agentOutput, request_dict.get('Price_Plan_Agent'))
		shared_response=AgentOutput(agentOutput=result)
		FinalOutput.finalOutput=result
		return shared_response

class Subproject_Creation_AgentInput(BaseModel):
	"""Input schema for Subproject_Creation_Agent."""

class Subproject_Creation_Agent(BaseTool):
	name: str = "Subproject_Creation_Agent Tool"
	description: str = (
		"Agent gonna execute the code under the file name AgentFunction.py"
	)
	args_schema: Type[BaseModel] = Subproject_Creation_AgentInput

	def _run(self) -> str:
		import AgentFunction
		importlib.reload(AgentFunction)
		from main import request_dict
		global shared_response
		result = AgentFunction.Subproject_Creation_Agent(shared_response.agentOutput, request_dict.get('Subproject_Creation_Agent'))
		shared_response=AgentOutput(agentOutput=result)
		FinalOutput.finalOutput=result
		return shared_response

class Summarize_AgentInput(BaseModel):
	"""Input schema for Summarize_Agent."""

class Summarize_Agent(BaseTool):
	name: str = "Summarize_Agent Tool"
	description: str = (
		"Agent gonna execute the code under the file name AgentFunction.py"
	)
	args_schema: Type[BaseModel] = Summarize_AgentInput

	def _run(self) -> str:
		import AgentFunction
		importlib.reload(AgentFunction)
		from main import request_dict
		global shared_response
		result = AgentFunction.Summarize_Agent(shared_response.agentOutput, request_dict.get('Summarize_Agent'))
		shared_response=AgentOutput(agentOutput=result)
		FinalOutput.finalOutput=result
		return shared_response

class TaskAssignmentGetEntityAgentInput(BaseModel):
	"""Input schema for TaskAssignmentGetEntityAgent."""

class TaskAssignmentGetEntityAgent(BaseTool):
	name: str = "TaskAssignmentGetEntityAgent Tool"
	description: str = (
		"Agent gonna execute the code under the file name AgentFunction.py"
	)
	args_schema: Type[BaseModel] = TaskAssignmentGetEntityAgentInput

	def _run(self) -> str:
		import AgentFunction
		importlib.reload(AgentFunction)
		from main import request_dict
		global shared_response
		result = AgentFunction.TaskAssignmentGetEntityAgent(shared_response.agentOutput, request_dict.get('TaskAssignmentGetEntityAgent'))
		shared_response=AgentOutput(agentOutput=result)
		FinalOutput.finalOutput=result
		return shared_response

class TaskAssignmentStepActionsAgentInput(BaseModel):
	"""Input schema for TaskAssignmentStepActionsAgent."""

class TaskAssignmentStepActionsAgent(BaseTool):
	name: str = "TaskAssignmentStepActionsAgent Tool"
	description: str = (
		"Agent gonna execute the code under the file name AgentFunction.py"
	)
	args_schema: Type[BaseModel] = TaskAssignmentStepActionsAgentInput

	def _run(self) -> str:
		import AgentFunction
		importlib.reload(AgentFunction)
		from main import request_dict
		global shared_response
		result = AgentFunction.TaskAssignmentStepActionsAgent(shared_response.agentOutput, request_dict.get('TaskAssignmentStepActionsAgent'))
		shared_response=AgentOutput(agentOutput=result)
		FinalOutput.finalOutput=result
		return shared_response

class TaskCompletion_AgentInput(BaseModel):
	"""Input schema for TaskCompletion_Agent."""

class TaskCompletion_Agent(BaseTool):
	name: str = "TaskCompletion_Agent Tool"
	description: str = (
		"Agent gonna execute the code under the file name AgentFunction.py"
	)
	args_schema: Type[BaseModel] = TaskCompletion_AgentInput

	def _run(self) -> str:
		import AgentFunction
		importlib.reload(AgentFunction)
		from main import request_dict
		global shared_response
		result = AgentFunction.TaskCompletion_Agent(shared_response.agentOutput, request_dict.get('TaskCompletion_Agent'))
		shared_response=AgentOutput(agentOutput=result)
		FinalOutput.finalOutput=result
		return shared_response

class checkServiceavailability_AgentInput(BaseModel):
	"""Input schema for checkServiceavailability_Agent."""

class checkServiceavailability_Agent(BaseTool):
	name: str = "checkServiceavailability_Agent Tool"
	description: str = (
		"Agent gonna execute the code under the file name AgentFunction.py"
	)
	args_schema: Type[BaseModel] = checkServiceavailability_AgentInput

	def _run(self) -> str:
		import AgentFunction
		importlib.reload(AgentFunction)
		from main import request_dict
		global shared_response
		result = AgentFunction.checkServiceavailability_Agent(shared_response.agentOutput, request_dict.get('checkServiceavailability_Agent'))
		shared_response=AgentOutput(agentOutput=result)
		FinalOutput.finalOutput=result
		return shared_response

