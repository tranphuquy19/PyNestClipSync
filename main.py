import asyncio
import socketio
import pyperclip

sio = socketio.AsyncClient(reconnection=True, reconnection_attempts=20, reconnection_delay=1)
rooms = open('rooms.txt', 'r').read().rstrip().split('\n')


@sio.event
async def connect():
    print('connected to server')
    for room in rooms:
        await sio.emit('join_room', room)
        print("You are in room: {0}".format(room))


@sio.event
async def disconnect():
    print('disconnected from server')


@sio.event
def msgToClient(msg):
    print(msg)


async def listen_clipboard():
    clipboard_content = ''
    while True:
        text = pyperclip.paste()
        if text != clipboard_content:
            clipboard_content = text
            print("new text from clipboard:", text)
            await sio.emit('msgToServer', {'rooms': rooms, 'payload': {'type': 'text', 'value': text}})
        await asyncio.sleep(1)


async def start_app():
    await sio.connect('http://localhost:3000')
    await sio.wait()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(start_app())
    loop.create_task(listen_clipboard())
    loop.run_forever()
