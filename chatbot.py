import nltk
from nltk.chat.util import Chat, reflections

# Define the chatbot's responses
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
        # ["I'm doing good. How about you?"]
    # ],
    [
        r"Tell me a joke",
        [" Sure! Why don't scientists trust atoms? Because they make up everything!"]
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
        r"quit",
        ["Bye! Take care."]
    ],
]]

# Create a chatbot
def chatbot():
    print("Hi! I am a chatbot. You can ask me anything.")

    # Create a chat instance
    chat = Chat(pairs, reflections)

    # Start chatting
    chat.converse()

if __name__ == "__main__":
    nltk.download('punkt')
    chatbot()
