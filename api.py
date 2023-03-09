from flask import Flask, jsonify, request
from flask_socketio import SocketIO
from flask_cors import CORS
from streambot import StreamBot
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", websocket=True)
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000","https://paisley-ui-hycvm.ondigitalocean.app"]}})

def chat_stream(messages):
    bot = StreamBot(os.getenv('OPENAI_KEY'), "Paisley", genesis_prompt="You are a helpful translator.")
    for event in bot.chat_stream(messages):
        yield event

messages = {}

@app.route('/api/getmessages/<user_id>', methods=['GET', 'POST'])
def get_messages(user_id):
    connection_id = user_id
    if connection_id in messages:
        return jsonify(messages)
    else:
        return jsonify([])

@app.route('/api/messages', methods=['GET', 'POST'])
def handle_messages():
    print("start handle_messages")
    print(request)
    connection_id = request.json.get('connection_id')
    print(connection_id)
    if request.method == 'GET':
        if connection_id in messages:
            return jsonify(messages[connection_id])
        else:
            return jsonify([])
    elif request.method == 'POST':
        if connection_id in messages:
            messages[connection_id].append({"role": "user", "content": request.json.get('message')})
        else:
            messages[connection_id] = [{"role": "user", "content": request.json.get('message')}]
        response = ""
        for event in chat_stream(messages[connection_id]):
            response += event
            socketio.emit('message', {'message': event}, broadcast=True)
        messages[connection_id].append({"role": "assistant", "content": response})
        return jsonify(messages[connection_id])

@app.route('/api/newchat', methods=['POST'])
def reset_chat():
    global messages
    connection_id = request.json.get('connection_id')
    if connection_id in messages:
        messages[connection_id] = []
    return jsonify(True)

if __name__ == '__main__':
    app.run(port=80)