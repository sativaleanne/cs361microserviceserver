# cs361microserviceserver
COMMUNICATION CONTRACT:

This server uses zeroMQ which uses sockets of type request and response to get messages. 
Binding the type response to a specific port will enable to client to recieve a message.

Requesting Data:
The client can request data by sending a message to the server. 
Example:

context = zmq.Context()

print("Connecting to server..")

socket = context.socket(zmq.REQ)

socket.connect("tcp://localhost:5555")

socket.send(b"Updated currency")

Recieving Data:
The client will recieve data by recieving a string back from the server.
Example:

the_data = socket.recv()

print("Received: [%s]" % (the_data))

UML sequence diagram:

![Sequence Diagram](https://user-images.githubusercontent.com/49132913/218278609-ba1a0fd3-ad90-4012-9897-81790500ddcb.png)
