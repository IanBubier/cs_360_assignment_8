import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:13579')

