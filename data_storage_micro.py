# Project: CS360 Assignment 8
# Title: Microservice A - Basic Account Management
# Author: Ian Bubier
# Date: 20/05/2024
# Description: A rudimentary account management microservice supporting basic CRUD functionality.

import json
import zmq
from pathlib import Path

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://localhost:13579')


def create(account, data):
    """
    Creates an account.
    :param account: any
    :param data: {'account': string, 'data': dictionary}
    :return: Success or common error string.
    """
    try:
        Path(f'Accounts/{account}').mkdir()
        for entry in data:
            with open(f'Accounts/{account}/{entry}.json', 'w') as create_entry:
                json.dump(data[entry], create_entry)
        func_return = f'{account} created.'
    except FileExistsError:
        func_return = 'FileExistsError'
    return func_return


def read(account, data=None):
    """
    Reads specified data from an account, or all data if data is None.
    :param account: any
    :param data: {'account': string, 'data': list or None}
    :return: Requested data dictionary or common error strings.
    """
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
        func_return = read_data
    except FileNotFoundError:
        func_return = 'FileNotFoundError'
    except PermissionError:
        func_return = 'PermissionError'
    return func_return


def update(account, data):
    """
    Updates an account.
    :param account: any
    :param data: {'account': string, 'data': dictionary}
    :return: Success or common error strings.
    """
    try:
        for entry in data:
            with open(f'Accounts/{account}/{entry}.json', 'w') as update_entry:
                json.dump(data[entry], update_entry)
        func_return = f'{account} updated.'
    except FileNotFoundError:
        func_return = 'FileNotFoundError'
    except PermissionError:
        func_return = 'PermissionError'
    return func_return


def delete(account, data=None):
    """
    Deletes specified data from an account, or deletes account and account data if data is None.
    :param account: any
    :param data: {'account': string, 'data': list or None}
    :return: Success or common error strings.
    """
    try:
        if data is None:
            data = Path(f'Accounts/{account}').iterdir()
            for entry in data:
                Path(entry).unlink()
            Path(f'Accounts/{account}').rmdir()
            func_return = f'{account} deleted.'
        else:
            for entry in data:
                Path(f'Accounts/{account}/{entry}.json').unlink()
            func_return = f'{data} deleted for {account}.'
    except FileNotFoundError:
        func_return = 'FileNotFoundError'
    except PermissionError:
        func_return = 'PermissionError'
    return func_return


while True:
    message = socket.recv_string()
    try:
        request = json.loads(message)
        if request == 'quit':
            reply = 'Ending Process.'
            reply = json.dumps(reply)
            socket.send_string(reply)
            break
        elif type(request) is not dict or len(request) != 3:
            reply = 'Invalid Message Format'
        else:
            try:
                account = request['account']
                operation = request['operation']
                data = request['data']
                if type(account) is not str:
                    reply = 'Invalid Account Format'
                elif type(operation) is not str:
                    reply = 'Invalid Operation Format'
                else:
                    valid_ops = ['create', 'read', 'update', 'delete']
                    if operation not in valid_ops:
                        reply = "Invalid Operation String"
                    elif operation == 'create' and type(data) is dict:
                        reply = create(account, data)
                    elif operation == 'read' and (type(data) is list or data is None):
                        reply = read(account, data)
                    elif operation == 'update' and type(data) is dict:
                        reply = update(account, data)
                    elif operation == 'delete' and (type(data) is list or data is None):
                        reply = delete(account, data)
                    else:
                        reply = 'Invalid Data Format'
            except KeyError:
                reply = 'KeyError'
    except json.JSONDecodeError:
        reply = 'JSONDecodeError'
    reply = json.dumps(reply)
    socket.send_string(reply)
