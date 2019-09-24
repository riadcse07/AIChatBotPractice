from ChatProcessor import ChatProcessor
import warnings

warnings.filterwarnings("ignore")
try:
    file = open('Corpas', 'r')
    cp = ChatProcessor(file.read())
except IOError:
    print("Error: can\'t find file or read data")
else:
    file.close()
    print(
        "VIRTUAL AGENT: I am a virtual agent. I will answer your queries about Bank Credit Cards. If you want to "
        "exit, type Bye!")
    while (True):
        input_text = input().lower()
        termination = ("bye", "thank")
        pro_data = cp.stem_sentence(input_text)
        if (termination[0] in pro_data):
            print("VIRTUAL AGENT: Bye! Take care.")
            break
        if (termination[1] in pro_data):
            print("VIRTUAL AGENT: You are welcome.")
            break
        ic = cp.initial_conversion(input_text)
        if (ic != None):
            print("VIRTUAL AGENT: " + ic)
            continue
        print("VIRTUAL AGENT: " + cp.bot_answer(input_text))
