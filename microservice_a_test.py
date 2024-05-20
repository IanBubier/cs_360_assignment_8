import zmq
import json
import time

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:13579')

test_account = 'Test User'
test_data = {'Key 1': 'Value 1', 'Key 2': 'Value 2', 'Key 3': 'Value 3'}

test_create = {'account': test_account, 'operation': 'create', 'data': test_data}
request = json.dumps(test_create)
socket.send_string(request)
reply = socket.recv_string()
print('Test program requests account creation. Microservice creates account and replies.')
print(json.loads(reply))
print('\n')
time.sleep(10)

test_read = {'account': test_account, 'operation': 'read', 'data': None}
request = json.dumps(test_read)
socket.send_string(request)
reply = socket.recv_string()
print('Test program requests account data and microservice replies with all account data.')
print(json.loads(reply))
print('\n')
time.sleep(10)

test_update = {'account': test_account, 'operation': 'update', 'data': {'Key 2': 'Value 4'}}
request = json.dumps(test_update)
socket.send_string(request)
reply = socket.recv_string()
print('Test program requests account data update. Microservice updates specified account data and replies.')
print(json.loads(reply))
print('\n')
time.sleep(10)

test_read = {'account': test_account, 'operation': 'read', 'data': ['Key 2']}
request = json.dumps(test_read)
socket.send_string(request)
reply = socket.recv_string()
print('Test program requests specific account data and microservice replies with specified data.')
print(json.loads(reply))
print('\n')
time.sleep(10)

test_delete = {'account': test_account, 'operation': 'delete', 'data': ['Key 1']}
request = json.dumps(test_delete)
socket.send_string(request)
reply = socket.recv_string()
print('Test program requests deletion of specific account data. Microservice deletes specified data and replies.')
print(json.loads(reply))
print('\n')
time.sleep(10)

test_read = {'account': test_account, 'operation': 'read', 'data': None}
request = json.dumps(test_read)
socket.send_string(request)
reply = socket.recv_string()
print('Test program requests account data and microservice replies with all account data.')
print(json.loads(reply))
print('\n')
time.sleep(10)

test_delete = {'account': test_account, 'operation': 'delete', 'data': None}
request = json.dumps(test_delete)
socket.send_string(request)
reply = socket.recv_string()
print('Test program requests account deletion. Microservice deletes account and replies.')
print(json.loads(reply))
print('\n')
time.sleep(10)

test_quit = 'quit'
request = json.dumps(test_quit)
socket.send_string(request)
reply = socket.recv_string()
print('Test program requests end of microservice and microservice ends.')
print(json.loads(reply))
print('\n')
