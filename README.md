This is a rudimentary data storage microservice supporting standard CRUD functionality.

The program will accept requests via JSON files sent through the assigned ZeroMQ pipe. The file must load a dictionary with three keys: 'account', 'operation', and 'data'. 'account' must be a string. 'operation' must be the strings 'create', 'read', 'update', or 'delete'. The program will perform the requested operation on the requested account. For 'create' operations, 'data' must be a dictionary of the information to be stored. For 'read' operations, 'data' may be a list of keys for which to retrieve data or None to retrieve all data. For 'update' operations, 'data' must be a dictionary of the information to update or store. For 'delete' operations, 'data' may be a list of keys to delete or None to delete the entire account. The exception to the three-key dictionary format is a JSON file containing the string 'quit', which will end the program.

EXAMPLE REQUEST:
test_account = 'Test User'
test_data = {'Key 1': 'Value 1', 'Key 2': 'Value 2', 'Key 3': 'Value 3'}
test_create = {'account': test_account, 'operation': 'create', 'data': test_data}
request = json.dumps(test_create)
socket.send_string(request)

The program will reply to requests via JSON files sent through the assigned ZeroMQ pipe. For 'create', 'read', or 'delete' operations, the reply will be a string containing a confirmation of success, a string containing the name of a likely error, or nothing if some other error occurred. For 'update' operations, the reply will be a dictionary containing the requested information, a string containing the name of a likely error, or nothing if some other error occurred.

EXAMPLE REPLY:
reply = socket.recv_string()
reply = json.loads(reply)

![basic_UML](https://github.com/IanBubier/cs_360_assignment_8/assets/137921511/35ad18bf-35a9-4639-865e-150f9e0a733a)
