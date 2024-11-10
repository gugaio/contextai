from dotenv import load_dotenv
from context import ConversationManager
from context.samples.player import PlaybackAPIAnalystAgent, FFMpegAgent

load_dotenv()

agents = [PlaybackAPIAnalystAgent(), FFMpegAgent()]
manager = ConversationManager(agents)

messages = []
while True:
    user = input("User: ")
    messages.append({"role": "user", "content": user})
    response_messages = manager.handle(messages)
    messages.extend(response_messages)
