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
    """Done!"""
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
    """Done!"""
    try:
        read_data = {}
        if data is None:
            for entry in Path(f'Accounts/{account}').iterdir():
                with open(entry, 'r') as read_entry:
                    entry_data = json.load(read_entry)
                    read_data[f'{entry.stem}'] = entry_data
        else:
            for entry in data:
                with open(f'Accounts/{account}/{entry}.json', 'r') as read_entry:
                    entry_data = json.load(read_entry)
                    read_data[entry] = entry_data
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
    """Done!"""
    try:
        for entry in data:
            with open(f'Accounts/{account}/{entry}.json', 'w') as update_entry:
                json.dump(data[entry], update_entry)
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
    """Done"""
    rmdir = False
    if data is None:
        data = Path(f'Accounts/{account}').iterdir()
        rmdir = True
    try:
        for entry in data:
            Path(entry).unlink()
        if rmdir is True:
            Path(f'Accounts/{account}').rmdir()
            with open('reply.json', 'w') as reply:
                json.dump(f'{account} deleted.', reply)
        else:
            with open('reply.json', 'w') as reply:
                json.dump(f'{data} deleted for {account}.', reply)
    except FileNotFoundError:
        with open('reply.json', 'w') as reply:
            json.dump('FileNotFoundError', reply)
    except PermissionError:
        with open('reply.json', 'w') as reply:
            json.dump('PermissionError', reply)


