import psutil

from flask import Flask
from flask import render_template
from flask_sockets import Sockets


app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/cpu')
def cpu_socket(ws):
    while not ws.closed:
        cpu_percent = psutil.cpu_percent(interval=3)
        ws.send(str(cpu_percent))

@app.route('/')
def hello():
   return render_template('index.html') 


if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
