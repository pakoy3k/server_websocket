#!/usr/bin/env python

#README
#install libraries
#pip install websockets


# WS server example


import asyncio
import websockets
import json
import base64

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"HOLA {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

async def hello_json(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")
    STATE = {"value": 0}

    greeting = json.dumps({"type": "state", **STATE})

    await websocket.send(greeting)
    print(f"> {greeting}")

async def main(websocket, path):
    data = open("base64.txt","r").read()
    decode = base64.b64decode(data) #comentar si no requieres la decodificacion
    await websocket.send(decode)    #cambiar decode por data
    print(f"> {decode}")

start_server = websockets.serve(main, "localhost", 1981)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
