from flask import Flask, request, Response
import os
import openai
import speech_recognition as sr
import sys

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.Completion()


def ask(incoming_msg):
    conversation = ""
    user_name = "You"
    bot_name = "Lenina"
    prompt = user_name + ": " + incoming_msg + "\n" + bot_name + ": "
    conversation += prompt
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=conversation, max_tokens=100
    )
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(user_name + ": ", 1)[0].split(bot_name + ": ", 1)[
        0
    ]
    conversation += response_str + "\n"
    return str(response_str)


def root_dir():
    return os.path.abspath(os.path.dirname(__file__))


def get_file(filename):
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)


@app.route("/lenina/answer", methods=["POST"])
def lenina():
    incoming_msg = request.get_json()["question"]
    answer = ask(incoming_msg)
    return answer


@app.route("/speech", methods=["GET"])
def speech():
    user_input = ""
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)
        try:
            user_input = r.recognize_google(audio, language="en-us")
        except:
            print("Exception occured while converting to audio to speech...")
            sys.exit(1)

    return user_input


@app.route("/", methods=["GET", "POST"])
def home():
    content = get_file("index.html")
    return Response(content, mimetype="text/html")


@app.route("/style.css", methods=["GET"])
def style():
    content = get_file("style.css")
    return Response(content, mimetype="text/css")


@app.route("/script.js", methods=["GET"])
def scriptjs():
    content = get_file("script.js")
    return Response(content, mimetype="text/js")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


# @app.route('/')
# def hello_world():
#     date = datetime.now()
#     return '@' + str(date)+ ': Hello, World!'
