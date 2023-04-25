import openai
import pyttsx3
import speech_recognition as sr
from api_key import API_KEY

openai.api_key = API_KEY
# engine = pyttsx3.init("dummy")

import speech_recognition as sr

print((sr.Microphone.list_microphone_names()))


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=3, phrase_time_limit=5)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-us")
        print("Let's talk about {}.".format(query))
    except Exception as e:
        print("voice not recognized")


takecommand()
