# Project: CS360 Group Project
# Title: Napoleon Microservice A
# Author: Ian Bubier
# Date: 18/05/2024
# Description: TODO

import json
import zmq
from pathlib import Path

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://localhost:13579')


def create(account, data):
    """TODO"""
    try:
        Path(f'Accounts/{account}').mkdir()
        for entry in data:
            with open(f'Accounts/{account}/{entry}.json', 'w') as create_entry:
                json.dump(data[entry], create_entry)
        with open('reply.json', 'w') as reply:
            json.dump(f'{account} created.', reply)
    except FileExistsError:
        with open('reply.json', 'w') as reply:
            json.dump('FileExistsError', reply)
    return reply


def read(account, data=None):
    """TODO"""
    if data is None:
        data = Path(f'Accounts/{account}').iterdir()
    try:
        read_data = {}
        for entry in data:
            read_data[entry] = json.dumps(f'Accounts/{account}/{entry}.json')
        with open('reply.json', 'w') as reply:
            json.dump(read_data, reply)
    except FileNotFoundError:
        with open('reply.json', 'w') as reply:
            json.dump('FileNotFoundError', reply)
    except PermissionError:
        with open('reply.json', 'w') as reply:
            json.dump('PermissionError', reply)
    return reply


def update(account, data):
    """TODO"""
    try:
        for entry in data:
            with open(f'Accounts/{account}/{entry}.json', 'w') as create_entry:
                json.dump(data[entry], create_entry)
        with open('reply.json', 'w') as reply:
            json.dump(f'{account} updated.', reply)
    except FileNotFoundError:
        with open('reply.json', 'w') as reply:
            json.dump('FileNotFoundError', reply)
    except PermissionError:
        with open('reply.json', 'w') as reply:
            json.dump('PermissionError', reply)
    return reply


def delete(account, data=None):
    """TODO"""
    if data is None:
        data = Path(f'Accounts/{account}').iterdir()
    try:
        for entry in data:
            Path(f'Accounts/{account}/{entry}.json').unlink()
        Path(account).rmdir()
        with open('reply.json', 'w') as reply:
            json.dump(f'{account} deleted.', reply)
    except FileNotFoundError:
        with open('reply.json', 'w') as reply:
            json.dump('FileNotFoundError', reply)
    except PermissionError:
        with open('reply.json', 'w') as reply:
            json.dump('PermissionError', reply)


test_data = {'test_key': 'test_value'}
create('test_account', test_data)
