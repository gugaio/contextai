from dotenv import load_dotenv
from conversation_manager import ConversationManager
from samples.player import PlaybackAPIAnalystAgent, FFMpegAgent

load_dotenv()

context = {}
agents = [PlaybackAPIAnalystAgent(context=context), FFMpegAgent(context=context)]

manager = ConversationManager()
manager.setup(agents, context)

messages = []
while True:
    user = input("User: ")
    messages.append({"role": "user", "content": user})

    response_messages = manager.handle(messages)

    messages.extend(response_messages)
