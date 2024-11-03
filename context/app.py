from dotenv import load_dotenv
from conversation_manager import ConversationManager
from agents import TriageAgent, PlaybackAPIAnalystAgent, FFMpegAgent

load_dotenv()


def agents(context):
    return [PlaybackAPIAnalystAgent(context=context), FFMpegAgent(context=context)]

def setup():
    context = {}
    map_agents = {agent.id: agent for agent in agents(context)}
    context["agents"] = map_agents
    triage_agent =TriageAgent(id="triage_agent",name="Triage Agent", task="", context=context, agents=map_agents)
    return triage_agent

initial_agent = setup()
manager = ConversationManager(initial_agent)

messages = []
while True:
    user = input("User: ")
    messages.append({"role": "user", "content": user})

    response = manager.handle(messages)

    messages.extend(response)
