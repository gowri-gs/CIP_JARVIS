import pyttsx3
import speech_recognition as sr
import datetime
import os
import sys
import wikipedia
import pyjokes
import aiml

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
BRAIN_FILE = "brain1.dump"
k = aiml.Kernel()
k.learn("std-startup.xml")
k.respond("LOAD AIML B")  # text to speech


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
# To convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=4, phrase_time_limit=5)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


# To wish
def wish():
    hour = datetime.datetime.now().hour
    if hour == 0 and hour <= 12:
        speak("good morning")
    elif hour>12 and hour<18:
        print("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis. please tell me how can i help you")

if __name__ == "__main__":
    #wish()
    i = 0
    # while True:
    while i != 1:
        query = takecommand().upper()
        # logic building for tasks
        if 'OPEN NOTEPAD' in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        elif "OPEN COMMAND PROMPT" in query:
            os.system("start cmd")
        elif "YOU CAN SLEEP" in query:
            speak("It is my pleasure!! Have a good day!")
            sys.exit()
            # to fetch information from wikipedia
        elif "WIKIPEDIA" in query:
            speak("Searching Wikipedia...")
            query = query.replace("Wikipedia", "")
            person = query.replace("Wikipedia", "")
            results = wikipedia.summary(person, sentences=2)
            speak(results)
            print(results)
        # to close notepad
        elif "CLOSE NOTEPAD" in query:
            speak("Okay, closing notepad")
            os.system("taskkill /F /IM notepad.exe")
        # to set alarm
        elif "SET ALARM" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = "F:\\Music"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
        elif "SHUTDOWN THE SYSTEM" in query:
            os.system("shutdown /s /t 1")
        elif "TELL ME A JOKE" in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif "RESTART THE SYSTEM" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        else:
            response = k.respond(query)
            speak(response)