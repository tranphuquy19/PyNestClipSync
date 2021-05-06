import asyncio
import socketio

sio = socketio.AsyncClient(reconnection=True, reconnection_attempts=20, reconnection_delay=1)

@sio.event
async def connect():
    print('connected to server')
    await sio.emit('msgToServer', 'test message')

@sio.event
async def disconnect():
    print('disconnected from server')

@sio.event
def msgToClient(msg):
    print(msg)

async def start_server():
    await sio.connect('http://localhost:3000')
    await sio.wait()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(start_server())
    loop.run_forever()
