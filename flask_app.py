import time
from flask import Flask, Response
flask_app = Flask(__name__)

@flask_app.route('/hello')
def hello_world():
    print('\ngot a request\n')
    return Response('Hello, World from Flask!', mimetype='text/plain')

app = flask_app.wsgi_app
