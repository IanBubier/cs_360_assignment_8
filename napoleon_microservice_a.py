# Project: CS360 Group Project
# Title: Napoleon Microservice A
# Author: Ian Bubier
# Date: 18/05/2024
# Description:

import json
import zmq
from pathlib import Path

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://localhost:13579')


def create(account, data):
    """DONE"""
    try:
        Path(account).mkdir()
        for entry in data:
            Path(f'{account}/{entry}.json').write_text(json.dumps(data[entry]))
        Path('reply.json').write_text(json.dumps(f'{account} created.'))
    except FileExistsError:
        with open('reply.json', 'w') as response:
            json.dump('FileExistsError', response)
    return response


def read(account, data=None):
    """"""
    if data is None:
        data = Path(account).iterdir()
    try:
        for entry in data:
            pass
        Path('reply.json').write_text(json.dumps(''))
    except FileNotFoundError:
        with open('reply.json', 'w') as response:
            json.dump('FileNotFoundError', response)
    except PermissionError:
        with open('reply.json', 'w') as response:
            json.dump('PermissionError', response)


def update(account, data):
    """DONE"""
    try:
        for entry in data:
            Path(f'{account}/{entry}.json').write_text(json.dumps(data[entry]))
        Path('reply.json').write_text(json.dumps(f'{account} updated.'))
    except FileNotFoundError:
        with open('reply.json', 'w') as response:
            json.dump('FileNotFoundError', response)
    except PermissionError:
        with open('reply.json', 'w') as response:
            json.dump('PermissionError', response)
    return response


def delete(account, data=None):
    """"""
    if data is None:
        data = Path(account).iterdir()
    try:
        for entry in data:
            Path(f'{account}/{entry}.json').unlink()
        Path(account).rmdir()
        Path('reply.json').write_text(json.dumps(f'{account} deleted.'))
    except FileNotFoundError:
        with open('reply.json', 'w') as response:
            json.dump('FileNotFoundError', response)
    except PermissionError:
        with open('reply.json', 'w') as response:
            json.dump('PermissionError', response)
