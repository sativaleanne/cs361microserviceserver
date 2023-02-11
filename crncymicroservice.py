import time
import zmq
from urllib.request import urlopen
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:

    message = socket.recv()
    print(f"Received request: {message}")

    url = "http://www.floatrates.com/daily/usd.json"
    response = urlopen(url)


    data = json.loads(response.read())

    jdata = json.dumps(data, indent=1)

    with open('usd_current.txt', 'w') as json_file:
        json_file.write(jdata)



    time.sleep(4)

    socket.send_string(jdata)
