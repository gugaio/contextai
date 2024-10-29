from openai import OpenAI
from agents import initial_agent, Agent


class Kernel:

    def __init__(self):
        self.client = OpenAI()
        self.current_agent = initial_agent()


    def run(self, messages):
        len_init_messages = len(messages)
        messages = messages.copy()
        self._completion_loop(messages)
        return messages[len_init_messages:]
    

    def _completion_loop(self, messages):
        while True:
            response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "system", "content": self.current_agent.instructions}] + messages,
                    tools=self.current_agent.tool_schemas() or None,
                )
            message = response.choices[0].message
            messages.append(message)
            if message.content: print("Assistant:", message.content)
            if not message.tool_calls:
                break
            tool_messages = self._execute_tools(message)
            messages.extend(tool_messages)

    def _execute_tools(self, message):
        tool_messages = []
        for tool_call in message.tool_calls:
            result = self.current_agent.execute_tool(tool_call)
            if type(result) is Agent:
                self.current_agent = result
                result = (
                    f"Transfered to {self.current_agent.name}. Adopt persona immediately."
                )

            tool_message = {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            }
            tool_messages.append(tool_message)
        return tool_messages