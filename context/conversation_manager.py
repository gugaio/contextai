from openai import OpenAI
from context.tools import ToolExecutor
from context.agents import TriageAgent

class ConversationManager:

    def __init__(self, agents:list):
        self._llm = OpenAI()
        self.context = {}
        self._setup(agents)

    def _setup(self, agents:list):
        for agent in agents:
            agent.context = self.context
        map_agents = {agent.id: agent for agent in agents}
        self.context["agents"] = map_agents
        self.triage_agent =TriageAgent(id="triage_agent",name="Triage Agent", task="", context=self.context, agents=map_agents)
        self.current_agent = self.triage_agent

    def handle(self, messages):
        messages, init_messages_count = self._copy_messages(messages)
        self._completion_loop(messages)
        return messages[init_messages_count:]

    def _completion_loop(self, messages):
        while True:
            response = self._invoke_llm(messages, self._current_agent_instruction() ,self._current_agent_tools())
            message = self._append_llm_response(messages, response)
            if not message.tool_calls:
                break
            tool_messages = self._execute_tools(message)
            messages.extend(tool_messages)

    def _execute_tools(self, message):
        tool_messages, final_agent  = ToolExecutor.execute_tools(message.tool_calls, self.current_agent)        
        self.current_agent = final_agent
        return tool_messages

    def _copy_messages(self, messages):
        return messages.copy(), len(messages)

    def _invoke_llm(self, messages, instructions, tools):
        messages_to_send = [{"role": "system", "content": instructions}] + messages
        return self._llm.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages_to_send,
            tools=tools,
        )
        
    def _append_llm_response(self, messages, response):
        message = response.choices[0].message
        messages.append(message)
        if message.content: print("Assistant:", message.content)
        return message
    
    def _current_agent_instruction(self):
        return self.current_agent.instructions()

    def _current_agent_tools(self):
        return self.current_agent.tool_schemas()