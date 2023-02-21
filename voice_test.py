import pyttsx3
import openpyscad as ops
from datetime import datetime
import os

name = input("What object do you want to create? ")
engine = pyttsx3.init()
engine.say("hi what is your name")
engine.runAndWait()