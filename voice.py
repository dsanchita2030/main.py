import sys
import time
import os
import pyttsx3
import speech_recognition as sr
global display
# display = []
# Defult Speak  ##############################################################################################

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # # print(voices[1].id)
    engine.setProperty('voice', voices[1].id)
    engine.setProperty("rate", 160)
    listener = sr.Recognizer()
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Lisiting and Recognizing System   ###################################################################################


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        # display.append()
        r.pause_threshold = 0.75
        audio = r.listen(source, phrase_time_limit=5)
        # audio = r.listen(source)
    try:
        # print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        # display = query

    except Exception as e:
        # speak('are you their, your voice not Recognize, say that Again.. ')
        return "none"
    query = query.lower()
    return query




# takecommand()
# speak('hi sanchita')
# welcome_en()