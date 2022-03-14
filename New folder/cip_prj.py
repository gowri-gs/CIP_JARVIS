import pyttsx3
import speech_recognition as sr
import datetime
import time
import os
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#To wish
def wish():
    hour = datetime.datetime.now().hour

    if hour==0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis. please tell me how can i help you")

#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sruthigowri000@gmail.com','Gowri@20002k')
    server.sendmail('sruthigowri000@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    wish()
    #while True:
    if 1:
        query = takecommand().lower()

        #logic building for tasks
        if 'open notepad' in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open adobe reader" in query:
            apath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "play music" in query:
            music_dir = "F:\\Music"
            songs = os.listdir(music_dir)
            r = random.choice(songs)
            os.startfile(os.path.join(music_dir,r))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open('www.youtube.com')

        elif "open facebook" in query:
            webbrowser.open('www.facebook.com')

        elif "open stackoverflow" in query:
            webbrowser.open('www.stackoverflow.com')

        elif "open google" in query:
            speak('Sir, What should I search on google')
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            now_time = time.localtime()
            hour = time.strftime("%H",now_time)
            hr = int(hour)
            min = time.strftime("%M", now_time)
            minute = int(min)
            minute+=2
            print(now_time)
            print(hour)
            print(min)
            kit.sendwhatmsg("+919364595644", "Hellooo Paaaa!! I am Gowri Kutty",hr,minute)

        elif "play song on youtube" in query:
            kit.playonyt("see you again")

        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takecommand().lower()
                to = 'mr.subashraja@gmail.com'
                sendEmail(to,content)
                speak("Email has been sent to Gayathri")

            except Exception as e:
                print(e)
                speak("Sorry Gowri, I am not able to send the email")

        elif "you can sleep" in query:
            speak("It is my pleasure!! Have a good day!")
            sys.exit()

    #to close notepad
        elif "close notepad" in query:
            speak("Okay, closing notepad")
            os.system("taskkill /f /im notepad.exe")

    #to set alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
                music_dir = "E:\\music"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))

    #to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

    # to shut down the system
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

    # to restart the system
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

    # to sleep the system
        elif "sleep the system" in query:
            os.system("rundl132.exe powrprof.dll,SetSuspendState 0,1,0")



        speak("Do you have any other task?")

