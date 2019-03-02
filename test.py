import socketio
import eventlet

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

sio.emit('movement', {'response': 'my refsdafsadfdsafassponse'})
sio.wait()



# sio = socketio.Server()
# app = socketio.WSGIApp(sio, static_files={
#     '/': {'content_type': 'text/html', 'filename': 'index.html'}
# })

# @sio.on('connect')
# def connect(sid, environ):
#     print('connect ', sid)

# @sio.on('subscribeToMovement')
# def message(sid, data):
#     print('subscribeToMovement ', data)

# @sio.on('disconnect')
# def disconnect(sid):
#     print('disconnect ', sid)

# if __name__ == '__main__':
#     eventlet.wsgi.server(eventlet.listen(('localhost', 8000)), app)
