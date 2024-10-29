from dotenv import load_dotenv
from kernel import Kernel

load_dotenv()

messages = []
kernel = Kernel()

while True:
    user = input("User: ")
    messages.append({"role": "user", "content": user})

    response = kernel.run(messages)

    messages.extend(response)
