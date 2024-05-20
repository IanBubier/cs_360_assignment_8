# Project: CS360 Group Project
# Title: Napoleon Microservice A
# Author: Ian Bubier
# Date: 20/05/2024
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
        reply = f'{account} created.'
    except FileExistsError:
        reply = 'FileExistsError'
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
        reply = read_data
    except FileNotFoundError:
        reply = 'FileNotFoundError'
    except PermissionError:
        reply = 'PermissionError'
    return reply


def update(account, data):
    """Done!"""
    try:
        for entry in data:
            with open(f'Accounts/{account}/{entry}.json', 'w') as update_entry:
                json.dump(data[entry], update_entry)
        reply = f'{account} updated.'
    except FileNotFoundError:
        reply = 'FileNotFoundError'
    except PermissionError:
        reply = 'PermissionError'
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
            reply = f'{account} deleted.'
        else:
            reply = f'{data} deleted for {account}.'
    except FileNotFoundError:
        reply = 'FileNotFoundError'
    except PermissionError:
        reply = 'PermissionError'
    return reply

#   with open('reply.json', 'w') as reply:
#   json.dump(func_return, reply)
