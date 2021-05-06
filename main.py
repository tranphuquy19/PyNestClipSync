import asyncio
import socketio
import signal
import sys

sio = socketio.AsyncClient(reconnection=True, reconnection_attempts=20, reconnection_delay=1)
rooms = open('rooms.txt', 'r').readlines()


@sio.event
async def connect():
    print('connected to server')
    for room in rooms:
        _room = room.rstrip()
        await sio.emit('join_room', _room)
        print("You are in room: {0}".format(_room))


@sio.event
async def disconnect():
    print('disconnected from server')


@sio.event
def msgToClient(msg):
    print(msg)


async def start_server():
    await sio.connect('http://localhost:3000')
    await sio.wait()


async def disconnect_server():
    await sio.disconnect()


def interrupt_handler(sig, frame):
    disconnect_server()
    print("Disconnected")
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, interrupt_handler)
    loop = asyncio.get_event_loop()
    loop.create_task(start_server())
    loop.run_forever()
    signal.pause()
