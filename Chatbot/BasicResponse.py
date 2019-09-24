import string

from nltk.chat.util import Chat, reflections


class BasicResponse:
    __pairs = [
        [
            r"hello|hi|greetings|what's up|hey",
            ["Hi", "Hey", "Glad to meet you", "Hi there", "Hello", "I am glad! You are talking to me"]
        ],
        [
            r"my name is (.*)|i am (.*)",
            ["Hello %1, How are you today ?", ]
        ],
        [
            r"who are you ?",
            ["Basically, I'm a chatbot. I will answer your queries about Bank Credit Card.", ]
        ],
        [
            r"i am (fine|good|well|great)",
            ["Glad to here it.", ]
        ],
        [
            r"what is your name ?",
            ["My name is iBot and I'm a chatbot ?", ]
        ],
        [
            r"how are you ?",
            ["I'm doing good\nHow about You ?", ]
        ],
        [
            r"sorry (.*)",
            ["Its alright", "Its OK, never mind", ]
        ],
        [
            r"i'm (.*) doing good",
            ["Nice to hear that", "Alright :)", ]
        ],
        [
            r"(.*) created ?",
            ["Bappy, Palash and Mahmud are created me", "top secret ;)", ]
        ]
    ]

    def __init__(self):
        self.chat = Chat(self.__pairs, reflections);

    @staticmethod
    def _get_punct():
        return dict((ord(punctuation), None) for punctuation in string.punctuation)

    def initial_conversion(self, text):
        try:
            text = text.lower().translate(self._get_punct())
            return self.chat.respond(text)
        except:
            return None
