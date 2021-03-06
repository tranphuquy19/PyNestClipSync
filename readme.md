# Python NestJS Clipboard Synchronization

Agents can use the Clipboard Synchronization feature to transfer text in both directions between devices, using Socket.io written in TypeScript and Python3

## Installation guide

* This project requires python >= 3.6 (client side), and NodeJS 12 (server side)

1. Clone this project

```bash
git clone https://github.com/tranphuquy19/PyNestClipSync.git
```

2. Install dependencies

```bash
cd PyNestClipSync
pip3 install python-socketio[client]==4.6.0 python-socketio[asyncio_client] pyperclip python-engineio==3.14.2 aiohttp
```

**Note**: If you are using linux OS please install `xclip` before moving on to the next step. By:

```bash
sudo apt install xclip -y # ubuntu, debian
sudo yum install xclip -y # centos, redhat
```

3. Add the room names you want to join to the file `rooms.txt`. Example:

```bash
public
my-room1
my-room2
```

**Note**: All messages of room `public` will be displayed at [https://clipsync.doramatching.tk](https://clipsync.doramatching.tk)

**Warning**: Be careful when copying sensitive data like `password`, `credentials`, etc. when you are in room `public`. Should name your room complicated to protect your sentitive data, example: `BYUuBui87jj`

4. Start the app

```bash
python3 main.py
```

![demo](/demo.png)
