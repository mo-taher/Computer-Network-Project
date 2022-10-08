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

while True:
    time.sleep(1)
    input_msg=input("How many hours did the Worker work:\n")
    
    if(input_msg == disconnect_message):
        send(disconnect_message)
        break
    
    send(input_msg)
        