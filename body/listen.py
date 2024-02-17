import speech_recognition #pip install speech_recognition
from googletrans import Translator # pip install googletrans==3.1.0a0




# listening function
def listen():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("LISTENING.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,8)

    try:
        print("RECOGNIZING.....")
        query  = r.recognize_google(audio,language='en')
    except Exception as e:
        print("SAY THAT AGAIN.")
        return ""
    return query

# translation fuction
def translationurtoeng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"USER : {data}.")
    return data

# connection b/w listening and translation
def micconnection():
    query = listen()
    data = translationurtoeng(query)
    return data

# micconnection()