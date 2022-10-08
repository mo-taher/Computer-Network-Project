import socket
import time

header = 16
port = 5050
server = socket.gethostbyname(socket.gethostname())
addr = (server, port)
format = 'utf-8'
disconnect_message ='end'
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(addr)

def send(msg):
    message = msg.encode(format)
    msg_length = len(message)
    send_length = str(msg_length).encode(format)
    send_length += b' ' * (header-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(format))

connected = True

while connected:
    time.sleep(0.5)
    input_msg = input("Input your text:  ")
    if(input_msg != disconnect_message):
        send(input_msg)
    else:
        connected = False
        send(disconnect_message)
        