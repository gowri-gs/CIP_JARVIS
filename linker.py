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
#from PyQt5.uic import loadUiType
from JarvisUI import Ui_MainWindow
import pywhatkit as kit
import mysql.connector
import functools
import operator


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

def linker(query):

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
    elif "RESTART THE SYSTEM" in query:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    else:
        response = k.respond(query)
        speak(response)