from flask import Flask, send_from_directory, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
from flask_cors import CORS
import webbrowser, threading, os, random

app = Flask(__name__)
CORS(app, origins="localhost")
socketio = SocketIO(app)



@app.route('/')
def serve_angular():
  return send_from_directory('./', 'index.html')


@app.errorhandler(404)
def http_error_handler(error):
  return serve_angular()


@app.errorhandler(500)
def server_error(e):
  return 'An internal error occurred [main.py] %s' % e, 500


@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)


@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@socketio.on('my json')
def handle_my_custom_event(data):
    emit('my response', data, broadcast=True)

def run_app():
  port = 1981
  threading.Timer(0.75, lambda: webbrowser.open('http://localhost:'+str(port))).start()
  socketio.run(app, host='localhost', port=port)