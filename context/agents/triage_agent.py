
from context.agents.base_agent import Agent

class TriageAgent(Agent):

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
                    "1. First, you need to know the video ID and player type. Ask users to provide both.\n"
                    " - unless the user has already provided these two information.\n"
                    "2. The follow are the tasks you can handle and the agent id to for:\n"
                    f"{instructions_to_transfer}"
                    "3. Ask what task user want and ONLY accept theses defined options, or ask user again.\n"
                    ""
                )
            
            return final_instruction
        
        def tools(self):
            return []