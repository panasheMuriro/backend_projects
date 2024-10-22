from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

# Handle incoming messages from clients
@socketio.on('message')
def handle_message(msg):
    print(f"Message: {msg}")
    # Broadcast message to all clients
    send(msg, broadcast=True)

# Run the app
if __name__ == '__main__':
    socketio.run(app, debug=True)
