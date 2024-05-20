import zmq
import json
import time
from pathlib import Path

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:13579')

test_account = 'test_user'
test_data = {'key_1': 'value_1', 'key_2': 'value_2', 'key_3': 'value_3'}

test_create = {'account': test_account, 'operation': 'create', 'data': test_data}
request = json.dumps(test_create)
socket.send_string(request)
reply = socket.recv_string()
reply = json.load(reply)
print(json.load(reply))
time.sleep(10)
