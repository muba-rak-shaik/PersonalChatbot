import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ["hi|hello", ["Hi there!", "Hello!"]],
    ["how are you", ["I'm doing well, thanks! How can I assist you?"]],
    ["what's your name", ["I'm a chatbot.", "I don't have a name."]],
    ["bye|goodbye", ["Goodbye!", "Have a great day!"]],
]

chatbot = Chat(pairs, reflections)
print("Chatbot: Hello! How can I help you today?")

while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
