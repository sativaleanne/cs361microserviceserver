import zmq

context = zmq.Context()

print("Connecting to server..")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

socket.send(b"Updated currency")

the_data = socket.recv()
print("Received: [%s]" % (the_data))


