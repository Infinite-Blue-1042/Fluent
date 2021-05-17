### CURRENTLY DOE NOT WORK: UNDER DEVOLPMENT
import socketio

sio.connect('http://localhost:5000')
sio = socketio.Client()

sio = socketio.AsyncClient()

@sio.event
def message(data):
    print('I received a message!')

@sio.on('my message')
def on_message(data):
    print('I received a message!')
    
@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")
    
sio.emit('my message', {'foo': 'bar'})
