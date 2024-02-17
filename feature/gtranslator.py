
from googletrans import Translator
import googletrans #pip install googletrans
from gtts import gTTS
import googletrans
import os
from playsound import playsound
import time
from body.speak import speak

def translategl(query):
    speak("SURE SIR")
    print(googletrans.LANGUAGES)
    translator = Translator()
    speak("Choose the language code in which you want to translate")
    b = input("Language code : ")   
    text_to_translate = translator.translate(query,src = "auto",dest= b,)
    text = text_to_translate.text
    try : 
        speakgl = gTTS(text=text, lang=b, slow= False)
        speakgl.save("voice.mp3")
        playsound("voice.mp3")
        
        time.sleep(5)
        os.remove("voice.mp3")
    except:
        print("Unable to translate")


