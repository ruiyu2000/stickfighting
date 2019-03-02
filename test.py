# from websocket import create_connection
# ws = create_connection("ws://10.168.74.81:8000/socket.io/?EIO=3&transport=websocket")
# print("Sending 'Hello, World'...")
# ws.send("subscribeToMovement")

import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('connection established')

@sio.on('subscribeToMovement')
def on_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.on('server')
def on_server(data):
    print('on server', data)

@sio.on('disconnect')
def on_disconnect():
    print('disconnected from server')

sio.connect('http://10.168.74.81:8000')

sio.emit('subscribeToMovement', {'response': 'my refsdafsadfdsafassponse'})
sio.wait()
