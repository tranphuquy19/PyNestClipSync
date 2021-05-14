import asyncio
import socketio
import pyperclip

sio = socketio.AsyncClient(reconnection=True, reconnection_attempts=20, reconnection_delay=1)
rooms = open('rooms.txt', 'r').read().strip().split('\n')


@sio.event
async def connect():
    print('connected to server')
    await sio.emit('join_room', rooms)
    print("Your ID: {0}".format(sio.sid))
    print("You are in rooms: {0}".format(rooms))


@sio.event
async def disconnect():
    print('disconnected from server')


@sio.event
def msgToClient(data):
    if data['from'] != sio.sid and data['value'] != pyperclip.paste():
        pyperclip.copy(data['value'])
        print(data['value'], 'from', data['from'])


async def listen_clipboard():
    clipboard_content = ''
    while True:
        text = pyperclip.paste()
        if text != clipboard_content:
            clipboard_content = text
            print("new text from clipboard:", text)
            await sio.emit('msgToServer', {'rooms': rooms, 'from': sio.sid, 'payload': {'type': 'text', 'value': text}})
        await asyncio.sleep(1)


async def start_app():
    await sio.connect('https://clipsync.doramatching.tk')
    await sio.wait()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(start_app())
    loop.create_task(listen_clipboard())
    loop.run_forever()
