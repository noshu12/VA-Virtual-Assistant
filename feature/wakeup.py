import speech_recognition as sr
import os

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en")

    except:
        return ""

    query = str(query).lower()
    print(query)
    return query

def wakeupdetected():
    queery = listen().lower()

    if "wake up" in queery:
        pass
        
    else:
        pass

while True:
    wakeupdetected()