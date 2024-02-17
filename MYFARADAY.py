# from brain.AIBrain import Replybrain
from body.listen import micconnection
from body.speak import speak
import webbrowser
import datetime
import pyautogui
import requests
from bs4 import BeautifulSoup 
import random
import os
from plyer import notification
import speedtest


print("")
print("")
print(">> Starting Faraday : Wait For Some Seconds.")
print("")
print("")
print("Firstly you should enter password :)")
speak("Firstly you should enter password :)")
print("")
for i in range(3):
    a = input("Enter Password to open FARADAY : ")
    pw_file = open("database\\password.txt","r")
    pw = pw_file.read() 
    pw_file.close()
    if (a==pw):
        print("")
        print("WELCOME SIR !")
        print("")
        print("Speak [WAKE UP] to start faraday, SIR")
        speak("Speak [WAKE UP] to start faraday, SIR")
        print("")
        break
    elif (i==2 and a!=pw): 
        print("SORRY SIR!, YOU HAD ENTER TOO MANY WRONG PASSWORD")
        speak("SORRY SIR!, YOU HAD ENTER TOO MANY WRONG PASSWORD")
        exit()

    elif (a!=pw):
        speak("Try Again, SIR")
        print("Try Again")
        
# for i in range(3):
#     a = input("Enter Password to open Jarvis :- ")
#     pw_file = open("password.txt","r")
#     pw = pw_file.read()
#     pw_file.close()
#     if (a==pw):
#         print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
#         break
#     elif (i==2 and a!=pw):
#         exit()

#     elif (a!=pw):
#         print("Try Again")


def MainExecution():
    if __name__ == "__main__":
                while True:
                    query = micconnection().lower()
                    if "go to sleep" in query:
                        speak("Ok SIR, You can me call anytime")
                        break 
                    elif "change password" in query:
                        speak("What's the new password")
                        new_pw = input("Enter the new password\n")
                        new_password = open("password.txt","w")
                        new_password.write(new_pw)
                        new_password.close()
                        speak("Done sir")
                        speak(f"Your new password is{new_pw}")

                    elif "set my day" in query:
                        tasks = [] #Empty list 
                        speak("Do you want to clear old tasks (Plz speak YES or NO)")
                        query = micconnection().lower()
                        if "yes" in query:
                            file = open("database\\task.txt","w")
                            file.write(f"")
                            file.close()
                            no_tasks = int(input("Enter the no. of tasks : "))
                            i = 0
                            for i in range(no_tasks):
                                tasks.append(input("Enter the task : "))
                                file = open("database\\task.txt","a")
                                file.write(f"{i}. {tasks[i]}\n")
                                file.close()
                        elif "no" in query:
                            i = 0
                            no_tasks = int(input("Enter the no. of tasks :- "))
                            for i in range(no_tasks):
                                tasks.append(input("Enter the task : "))
                                file = open("database\\task.txt","a")
                                file.write(f"{i}. {tasks[i]}\n")
                                file.close()
                    elif "show my day" in query:
                        file = open("database\\task.txt","r")
                        content = file.read()
                        file.close()
                        notification.notify(
                            title = "My schedule :",
                            message = content,
                            timeout = 15
                            )
                    # elif "open" in query:   #EASY METHOD
                    #     query = query.replace("open","")
                    #     query = query.replace("jarvis","")
                    #     pyautogui.press("super")
                    #     pyautogui.typewrite(query)
                    #     pyautogui.sleep(2)
                    #     pyautogui.press("enter") 
                    elif "translate" in query:
                        from feature.gtranslator import translategl
                        query = query.replace("jarvis","")
                        query = query.replace("translate","")
                        translategl(query)
                    elif "internet speed" in query:
                        wifi  = speedtest.Speedtest()
                        upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                        download_net = wifi.download()/1048576
                        print("Wifi Upload Speed is", upload_net)
                        print("Wifi download speed is ",download_net)
                        speak(f"Wifi download speed is {download_net}")
                        speak(f"Wifi Upload speed is {upload_net}")
                    elif "play a game" in query:
                        from brain.game import game_play
                        game_play()
                    elif "hello" in query:
                        speak("Hello, how are you ?, SIR")
                    elif "i am fine" in query:
                        speak("that's great, SIR")
                    elif "how are you" in query:
                        speak("Perfect, sir")
                    elif "thank you" in query:
                        speak("you are welcome, SIR")
                    elif "stop" in query:
                        pyautogui.press("k")
                        speak("video paused, SIR")
                    elif "play" in query:
                        pyautogui.press("k")
                        speak("video played, SIR")
                    elif "mute" in query:
                        pyautogui.press("m")
                        speak("video muted, SIR")
                    elif "unmute" in query:
                        pyautogui.press("m")
                        speak("video unmuted, SIR")
                    elif "full screen" in query:
                        pyautogui.press("f")
                        speak("full screen video, SIR")
                    elif "small screen" in query:
                        pyautogui.press("t")
                        speak("samll screen video , SIR")
                    elif "mini screen" in query:
                        pyautogui.press("i")
                        speak("mini screen video, SIR")
                    elif "captions on" in query:
                        pyautogui.press("c")
                        speak("caption on, SIR")
                    elif "captions off" in query:
                        pyautogui.press("c")
                        speak("caption off, SIR")
                    elif "next" in query:
                        pyautogui.hotkey("shift","N")
                        speak("Next video, SIR")
                    elif "click my photo" in query:
                        pyautogui.press("super")
                        pyautogui.typewrite("camera")
                        pyautogui.press("enter")
                        pyautogui.sleep(2)
                        speak("SMILE")
                        pyautogui.press("enter")
                    elif "screenshot" in query:
                        im = pyautogui.screenshot()
                        im.save("ss.jpg")
                    elif "news" in query:
                        from feature.NewsRead import latestnews
                        latestnews()
                    elif "volume up" in query:
                        from feature.keyboard import volumeup
                        speak("Turning volume up, SIR")
                        volumeup()
                    elif "volume down" in query:
                        from feature.keyboard import volumedown
                        speak("Turning volume down, SIR")
                        volumedown()
                    elif "open" in query:
                        from feature.Dictapp import openappweb
                        openappweb(query)
                    elif "close" in query:
                        from feature.Dictapp import closeappweb
                        closeappweb(query)

                    elif "google" in query:
                        from feature.Search import searchGoogle
                        searchGoogle(query)
                    elif "youtube" in query:
                        from feature.Search import searchYoutube
                        searchYoutube(query)
                    elif "wikipedia" in query:
                        from feature.Search import searchWikipedia
                        searchWikipedia(query)
                    elif "temperature" in query:
                        search = "temperature in karachi"
                        url = f"https://www.google.com/search?client=opera&q={search}"
                        r  = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        temp = data.find("div", class_ = "BNeawe").text
                        speak(f"current{search} is {temp}")
                    elif "weather" in query:
                        search = "weather in karachi"
                        url = f"https://www.google.com/search?client=opera&q={search}"
                        r  = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        temp = data.find("div", class_ = "BNeawe").text
                        speak(f"current{search} is {temp}")
                    elif "time" in query:
                        strTime = datetime.datetime.now().strftime("%H:%M")    
                        speak(f"Sir, the time is {strTime}")
                    elif "finally sleep" in query:
                        print("Bye! It was nice talking to you., SIR")
                        speak("Bye! It was nice talking to you., SIR")
                        exit()
                    elif "remember that" in query:
                        rememberMessage = query.replace("remember that","")
                        rememberMessage = query.replace("jarvis","")
                        speak("You told me"+rememberMessage)
                        remember = open("Remember.txt","a")
                        remember.write(rememberMessage)
                        remember.close()
                    elif "what do you remember" in query:
                        remember = open("Remember.txt","r")
                        speak("You told me" + remember.read())
                    elif "tired" in query:
                        speak("Playing your favourite songs, sir")
                        a = (1,2,3,4,5,6,7,8) # You can choose any number of songs (I have only choosen 3)
                        b = random.choice(a)
                        if b==1:
                            webbrowser.open("https://www.youtube.com/watch?v=CtCaNtFTxNU")
                        elif b==2:
                            webbrowser.open("https://www.youtube.com/watch?v=KvqjsROmyik")
                        elif b==3:
                            webbrowser.open("https://www.youtube.com/watch?v=sR0n6MgxcuI")
                        elif b==5:
                            webbrowser.open("https://www.youtube.com/watch?v=rgGDTO8g2Pg&t=61s")
                        elif b==6:
                            webbrowser.open("https://www.youtube.com/watch?v=RQIJMRmbphU")
                        elif b==7:
                            webbrowser.open("https://www.youtube.com/watch?v=A0F9MFGdb4M")
                    elif "shutdown the system" in query:
                        speak("Are You sure you want to shutdown")
                        shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                        if shutdown == "yes":
                            os.system("shutdown /s /t 1")

                        elif shutdown == "no":
                            break
                    else:
                        while True:
                            Replybrain(query)
                            Reply = Replybrain(query)
                            print(f"==> FARADAY AI : {Reply}")
                            speak(Reply)

def WakeupDetector():

    while True:
        query = micconnection().lower()
        if "Wake Up".lower() in query.lower():
            print("")
            print(">> Wake UP Detected!! >>")
            speak(">> Wake UP Detected!! >>")
            print("")
            from body.greet import greetMe
            greetMe()
            MainExecution()
        
    

WakeupDetector()
