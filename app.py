from flask import Flask
from datetime import datetime
import chatbot

app = Flask(__name__)

@app.route('/')
def hello_world():
    date = datetime.now()
    return '@' + str(date)+ ': Hello, World!'

@app.route('/chat')
def otherroute():
    # date = datetime.now()
    val = chatbot.fun()
    return val

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080)