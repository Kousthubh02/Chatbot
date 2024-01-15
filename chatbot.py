import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot. You can call me Chatbot."]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?"]
    ],
    [
        r"tell me a joke",
        ["Sure! Why don't scientists trust atoms? Because they make up everything!"]
    ],
    [
        r"i am fine",
        ["Good to know"]
    ],
    [
        r"sorry (.*)",
        ["No problem"]
    ],
    [
        r"bye",
        ["Bye! Take care."]
    ],
]

def chatbot():
    print("Hi! I am a chatbot. You can ask me anything.")
    chat = Chat(pairs, reflections)

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Bye! Take care.")
            break
        response = chat.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    nltk.download('punkt')
    chatbot()
