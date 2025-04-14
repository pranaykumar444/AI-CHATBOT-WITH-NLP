import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ["hi|hello", ["Hello!", "Hi there!"]],
    ["what is your name?", ["I'm CodTechBot."]],
    ["how are you?", ["I'm doing well. What about you?"]],
    ["(.*) your name?", ["My name is CodTechBot."]],
    ["bye", ["Goodbye!", "See you later!"]],
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
