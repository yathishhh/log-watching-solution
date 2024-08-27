
import time
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading
from collections import deque

app = Flask(__name__)
socketio = SocketIO(app)

log_file_path = 'log.txt'  
lines_to_show = 10
log_buffer = deque()

def get_last_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return lines[-n:]

@app.route('/log')
def log():
    last_lines = get_last_n_lines(log_file_path, lines_to_show)
    return render_template('index.html', log_lines=last_lines)

def tail_log_file():
    with open(log_file_path, 'r') as file:
        file.seek(0, 2)  

        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)
                continue
            log_buffer.append(line.strip())
            socketio.emit('log_update', {'data': line.strip()})

# @socketio.on('connect')
# def send_initial_lines():
#     for line in log_buffer:
#         emit('log_update', {'data': line})

if __name__ == '__main__':
    log_thread = threading.Thread(target=tail_log_file)
    log_thread.daemon = True
    log_thread.start()

    socketio.run(app, debug=True)


