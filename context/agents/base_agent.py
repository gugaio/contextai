from abc import abstractmethod
from typing import Optional
from pydantic import BaseModel
import json
from tools import function_to_schema

class Agent():

    def __init__(self, id: str, name: str, task: str, context: dict, agents: Optional[dict] = None):
        self.id = id
        self.name = name
        self.task = task
        self.context = context
        self.agents = agents

    @abstractmethod
    def tools(self) -> list:
        pass

    @abstractmethod
    def instructions(self) -> str:
        pass

    def transfer_to_agent(self, id):
            """Transfer to agent tool."""
            return self.context["agents"][id]

    def tool_schemas(self):
        tools = [self.transfer_to_agent] + self.tools()
        return [function_to_schema(tool) for tool in tools]
            
    def tools_map(self):
        tools = [self.transfer_to_agent] + self.tools()
        return {tool.__name__: tool for tool in tools}
    
    def execute_tool(self, tool_call):
        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)
        tools_map = self.tools_map()
        if name not in tools_map:
            return f"Tool {name} not found in agent {self.name}"

        print(f"Executing tool: {name} with args: {args}")
        return tools_map[name](**args)