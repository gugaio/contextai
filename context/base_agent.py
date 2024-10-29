from typing import Optional
from pydantic import BaseModel
import json
from tooling import function_to_schema

class Agent(BaseModel):
    """Agent model."""
    name: str = "Agent"
    instructions: str = "You are a helpful Agent"
    tools: list = []

    def tool_schemas(self):
        return [function_to_schema(tool) for tool in self.tools]
            
    def tools_map(self):
        return {tool.__name__: tool for tool in self.tools}
    
    def execute_tool(self, tool_call):
        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        print(f"Executing tool: {name} with args: {args}")
        return self.tools_map()[name](**args)