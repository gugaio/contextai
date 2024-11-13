from dotenv import load_dotenv
from context import ConversationManager
from context.samples.jurus import JurusAgent

load_dotenv()

initial_triage_instruction =  (
    "1. First you need to know the broker what user want to talk about\n"
    " - unless the user has already provided it\n"
)

manager = ConversationManager([JurusAgent()], initial_triage_instruction)

messages = []
while True:
    user = input("User: ")
    messages.append({"role": "user", "content": user})
    response_messages = manager.handle(messages)
    messages.extend(response_messages)
