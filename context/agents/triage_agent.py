
from context.agents.base_agent import Agent

class TriageAgent(Agent):
        
        ID = "triage_agent"
        NAME = "Triage Agent"
        TASK = "triage the user to the right agent or tool"

        def __init__(self, context: dict, agents: list, initial_custom_instruction: str):
            super().__init__(id=self.ID, name=self.NAME, task=self.TASK)
            self.context = context
            self.agents = agents
            self.initial_custom_instruction = initial_custom_instruction

        def instructions(self):

            instructions_to_transfer = ""
            for agent in self.agents.values():
                new_instruction = f'If the task is {agent.task}, call transfer to agent tool with id {agent.id}. \n'
                instructions_to_transfer += new_instruction

            final_instruction = (
                    "You are a triage agent."
                    "You goal is to help users execute the right agent or tool."
                    "Always answer in a sentence or less."
                    "Follow the following routine with the user:"
                    f"{self.initial_custom_instruction}"
                    "2. The follow are the tasks you can handle and the agent id to for:\n"
                    f"{instructions_to_transfer}"
                    "3. Ask what task user want and ONLY accept theses defined options, or ask user again.\n"
                    ""
                )
            
            return final_instruction
        
        def tools(self):
            return []