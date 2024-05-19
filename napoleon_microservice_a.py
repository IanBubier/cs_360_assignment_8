# Project: CS360 Group Project
# Title: Napoleon Microservice A
# Author: Ian Bubier
# Date: 18/05/2024
# Description:

import json
import zmq
from pathlib import Path

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:13579')

def account_management(account, instructions):
    """description"""

    if instructions['operation'] == 'check':
        if Path.is_dir(account):
            with open('reply.json', 'w') as outgoing:
                json.dump('Account does exist.', outgoing)
        else:
            with open('reply.json', 'w') as outgoing:
                json.dump('Account does not exist.', outgoing)

    elif instructions['operation'] == 'create':
        try:
            Path.mkdir(account)
            with open('reply.json', 'w') as outgoing:
                json.dump(f'{account} created.', outgoing)
        except FileExistsError:
            with open('reply.json', 'w') as outgoing:
                json.dump('FileExistsError', outgoing)

    elif instructions['operation'] == 'update':
        try:

        except FileNotFoundError:
            with open('reply.json', 'w') as outgoing:
                json.dump('FileNotFoundError', outgoing)
        except PermissionError:
            with open('reply.json', 'w') as outgoing:
                json.dump('PermissionError', outgoing)

    elif instructions['operation'] == 'delete':
        try:
            for file in Path.iterdir(account):
                Path.unlink(file)
            Path.rmdir(account)
            with open('reply.json', 'w') as outgoing:
                json.dump(f'{account} deleted.', outgoing)
        except FileNotFoundError:
            with open('reply.json', 'w') as outgoing:
                json.dump('FileNotFoundError', outgoing)
        except PermissionError:
            with open('reply.json', 'w') as outgoing:
                json.dump('PermissionError', outgoing)

    else:
        with open('reply.json', 'w') as outgoing:
            json.dump('Operation is invalid.', outgoing)

    return outgoing


while True:
    with open(f'{socket.recv_json()}', 'r') as message:
        incoming = json.load(message)
        try:
            socket.send_json(account_management(incoming['account'], incoming['instructions']))
        except KeyError:
            with open('reply.json', 'w') as outgoing:
                json.dump('KeyError', outgoing)