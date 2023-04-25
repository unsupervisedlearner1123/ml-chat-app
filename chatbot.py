import openai
import pyttsx3
import speech_recognition as sr
from api_key import API_KEY

openai.api_key = API_KEY
engine = pyttsx3.init()
# print((sr.Microphone.list_microphone_names()))


r = sr.Recognizer()
conversation = ""
user_name = "You"
bot_name = "Lenina"

while True:
    with sr.Microphone(device_index=1) as source:
        print("\nListening....")
        # r.adjust_for_ambient_noise(source, duration=0.2)
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)
        # audio = r.listen(source, timeout=3, phrase_time_limit=5)

    try:
        print("Recognizing....")
        user_input = r.recognize_google(audio, language="en-us")
        print("Lets talk about: {}.".format(user_input))
    except:
        continue

    prompt = user_name + ": " + user_input + "\n" + bot_name + ": "
    conversation += prompt

    # fetch response from open AI api
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=conversation, max_tokens=100
    )
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(user_name + ": ", 1)[0].split(bot_name + ": ", 1)[
        0
    ]
    conversation += response_str + "\n"
    print(response_str)

    engine.say(response_str)
    engine.runAndWait()
