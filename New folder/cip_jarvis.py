import pyttsx3
import speech_recognition as sr
import datetime
import os
import sys
import aiml
import pyautogui
import time
import requests
import smtplib
import random
import wikipedia
import webbrowser
import pyjokes
import csv
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
import json
from urllib.request import urlopen
import PyPDF2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTime, QTimer, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JarvisUI import Ui_MainWindow
import pywhatkit as kit

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

BRAIN_FILE = "brain1.dump"

k = aiml.Kernel()
k.learn("std-startup.xml")
k.respond("LOAD AIML B")

# Convert text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# To wish
def wish():
    hour = datetime.datetime.now().hour

    if hour == 0 and hour <= 12:
        speak("good morning")
    elif hour > 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis. please tell me how can i help you")

#Convert text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#News Generation
def NewsFromBBC():
    url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=22755c002c1e43bdba6ac9af021b90ff"
    main_page = requests.get(url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

#Read PDF
def pdfreader():
    speak("Where is the file located? Please enter it in the console")
    filelocation = input("Enter the file path:")
    book = open(filelocation, 'rb')
    pdf_Reader = PyPDF2.PdfFileReader(book)
    pages = pdf_Reader.numPages
    speak(f"There are {pages} number of pages in total in this book")
    speak("Enter the page number that is to be read")
    pg = int(input("Please enter the page number:"))

    page = pdf_Reader.getPage(pg)
    text = page.extractText()
    re.sub(r'(\r\n){2,}', '', text)
    re.sub(r'[^\w\s]', ' ', text)
    speak(text)

'''
if __name__ == "__main__":
    wish()
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

        elif "RESTART THE SYSTEM" in query:
            os.system("shutdown /r /t 5")

        elif "SLEEP THE SYSTEM" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "SWITCH THE WINDOW" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "TELL ME NEWS" in query:
            speak("Fetching the latest news...")
            NewsFromBBC()

        elif "EMAIL TO " in query:
            speak("What should I say?")
            query = takecommand().lower()
            if "send the file" in query:
                email = "sruthigowri000@gmail.com"
                password = "Gowri@20002k"
                sendemail = "sruthigowri2000@gmail.com";
                speak("Okay. What is the subject for this mail?")
                query = takecommand().lower()
                subject = query
                speak("Okay. What is the Message for this mail?")
                query2 = takecommand().lower()
                message = query2
                speak("Please enter the correct path of the file into the shell")
                fileloc = input("Enter the file path here")
                speak("I am sending the Mail now")

                msg = MIMEMultipart()
                msg["From"] = email
                msg["To"] = sendemail
                msg["Subject"] = subject
                msg.attach(MIMEText(message, 'plain'))

                # FILE ATTACHMENT
                filename = os.path.basename(fileloc)
                attachment = open(fileloc, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content_Disposition", "attachment; filemame=%s" % filename)

                # ATTACHING THE ATTACHMENT
                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, sendemail, text)
                server.quit()
                speak('Email has been sent successfully')

            else:
                email = "sruthigowri000@gmail.com"
                password = "Gowri@20002k"
                sendemail = "sruthigowri2000@gmail.com";
                message = query

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                server.sendmail(email, sendemail, message)
                server.quit()
                speak('Email has been sent successfully')

        elif "WHERE AM I" in query or "WHERE ARE WE" in query:
            speak("Wait Lemme check")
            try:
                url = 'http://ipinfo.io/json'
                response = urlopen(url)
                data = json.load(response)
                city = data['city']
                state = data['region']
                speak(f"We are in {city} city in {state} state")
            except Exception as e:
                speak("Due to network issue, I am not able to find where we are.. Sorry")
                pass

        elif "TAKE SNIPPET" in query or "TAKE SCREENSHOT" in query or "TAKE A SNIPPET" in query or "TAKE A SCREENSHOT" in query:
            speak("Tell me the name of this screenshot")
            name = takecommand().lower()
            speak("Please hold the screen for few seconds I am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"F:\\Sem 6\\CIP\\Pictures\\{name}.jpg")
            speak("The screenshot is saved in Pictures.. Now I am ready for next command")

        elif "READ THE PDF FILE" in query or "READ PDF FILE" in query or "READ PDF" in query:
            pdfreader()


        else:
            response = k.respond(query)
            speak(response)
            
'''

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    # To convert voice to text
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=1, phrase_time_limit=5)

        try:
            print("Recognising...")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"user said: {self.query}")

        except Exception as e:
            speak("Say that again please...")
            return "none"
        return self.query

    def TaskExecution(self):
        wish()
        i=0
        #while True:
        while i!=1:
            self.query = self.takecommand().upper()
            # logic building for tasks
            # to open notepad
            if 'OPEN NOTEPAD' in self.query:
                npath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)

            #to close notepad
            elif "CLOSE NOTEPAD" in self.query:
                speak("Okay, closing notepad")
                os.system("taskkill /F /IM notepad.exe")

            #to open command prompt
            elif "OPEN COMMAND PROMPT" in self.query:
                os.system("start cmd")

            # to set alarm
            elif "SET ALARM" in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn == 22:
                    music_dir = "F:\\Music"
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))

            #to shutdown the system
            elif "SHUTDOWN THE SYSTEM" in self.query:
                os.system("shutdown /s /t 1")

            #to restart the system
            elif "RESTART THE SYSTEM" in self.query:
                os.system("shutdown /r /t 5")

            #to sleep the system
            elif "SLEEP THE SYSTEM" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            #to switch the window
            elif "SWITCH THE WINDOW" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            #to fetch current news
            elif "TELL ME NEWS" in self.query:
                speak("Fetching the latest news...")
                NewsFromBBC()

            #to send a mail
            elif "EMAIL TO " in self.query:
                speak("What should I say?")
                self.query1=self.takecommand().lower()
                if "send the file" in self.query1:
                    email="sruthigowri000@gmail.com"
                    password="Gowri@20002k"
                    sendemail="sruthigowri2000@gmail.com";
                    speak("Okay. What is the subject for this mail?")
                    self.query1=self.takecommand().lower()
                    subject=self.query1
                    speak("Okay. What is the Message for this mail?")
                    self.query2 = self.takecommand().lower()
                    message = self.query2
                    speak("Please enter the correct path of the file into the shell")
                    fileloc=input("Enter the file path here")
                    speak("I am sending the Mail now")

                    msg=MIMEMultipart()
                    msg["From"]=email
                    msg["To"]=sendemail
                    msg["Subject"]=subject
                    msg.attach(MIMEText(message,'plain'))

                    #FILE ATTACHMENT
                    filename = os.path.basename(fileloc)
                    attachment=open(fileloc,"rb")
                    part=MIMEBase('application','octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header("Content_Disposition","attachment; filemame=%s" % filename)

                    #ATTACHING THE ATTACHMENT
                    msg.attach(part)

                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login(email,password)
                    text=msg.as_string()
                    server.sendmail(email,sendemail,text)
                    server.quit()
                    speak('Email has been sent successfully')

                else:
                    email = "sruthigowri000@gmail.com"
                    password = "Gowri@20002k"
                    sendemail = "sruthigowri2000@gmail.com";
                    message=self.query

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    server.sendmail(email, sendemail, message)
                    server.quit()
                    speak('Email has been sent successfully')

            #to find location
            elif "WHERE AM I" in self.query or "WHERE ARE WE" in self.query:
                speak("Wait Lemme check")
                try:
                    url = 'http://ipinfo.io/json'
                    response = urlopen(url)
                    data = json.load(response)
                    city = data['city']
                    state = data['region']
                    speak(f"We are in {city} city in {state} state")
                except Exception as e:
                    speak("Due to network issue, I am not able to find where we are.. Sorry")
                    pass

            #to take snippet
            elif "TAKE SNIPPET" in self.query or "TAKE SCREENSHOT" in self.query or "TAKE A SNIPPET" in self.query or "TAKE A SCREENSHOT" in self.query:
                speak("Tell me the name of this screenshot")
                name=self.takecommand().lower()
                speak("Please hold the screen for few seconds I am taking screenshot")
                time.sleep(3)
                img=pyautogui.screenshot()
                img.save(f"F:\\Sem 6\\CIP\\Pictures\\{name}.jpg")
                speak("The screenshot is saved in Pictures.. Now I am ready for next command")

            #to read a pdf file
            elif "READ THE PDF FILE" in self.query or "READ PDF FILE" in self.query or "READ PDF" in self.query:
                pdfreader()

            #to send a whatsapp message
            elif "SEND MESSAGE" in self.query:
                now_time = time.localtime()
                hour = time.strftime("%H", now_time)
                hr = int(hour)
                min = time.strftime("%M", now_time)
                minute = int(min)
                minute += 1
                #print(now_time)
                #print(hour)
                #print(min)
                speak("Whom should I send the message?")
                receiver = self.takecommand().lower()
                with open("F:\\Sem 6\\CIP\\contacts.csv","r") as f:
                    data=csv.reader(f)
                    for col in data:
                        print(col[0])
                kit.sendwhatmsg("+918825723971",
                                "Hellooo Paaaa!! I am Gowri Kutty", hr, minute)

            #to play music
            elif "PLAY MUSIC" in self.query:
                music_dir = "F:\\Music"
                songs = os.listdir(music_dir)
                r = random.choice(songs)
                os.startfile(os.path.join(music_dir, r))

            #to fetch information from wikipedia
            elif "WIKIPEDIA" in self.query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak(results)
                print(results)

            #to open youtube
            elif "OPEN YOUTUBE" in self.query:
                webbrowser.open('www.youtube.com')

            # to open facebook
            elif "OPEN FACEBOOK" in self.query:
                webbrowser.open('www.facebook.com')

            # to open stackoverflow
            elif "OPEN STACKOVERFLOW" in self.query:
                webbrowser.open('www.stackoverflow.com')

            #to open google
            elif "OPEN GOOGLE" in self.query:
                speak('Sir, What should I search on google')
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")

            #to play song on youtube
            elif "PLAY SONG ON YOUTUBE" in self.query:
                kit.playonyt("Sorry")

            # to tell a joke
            elif "TELL ME A JOKE" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            #to sleep jarvis
            elif "YOU CAN SLEEP" in self.query:
                speak("It is my pleasure!! Have a good day!")
                sys.exit()

            else:
                response = k.respond(self.query)
                speak(response)

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie =QtGui.QMovie("F:/Sem 6/CIP/GIF/Main.gif")
        self.ui.JarvisGUI.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("F:/Sem 6/CIP/GIF/Initialise.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
