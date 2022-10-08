import socket 

header = 16 
port = 5050  
Server = socket.gethostbyname(socket.gethostname()) # To fetch the devices IP address
addr = (Server, port) # Binding the IP address
format = "utf-8" # Format in which encoding and decoding will take place
disconnect_message = "End" # To show termination

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr) 

def send(msg):
    message = msg.encode(format)
    msg_len = len(message)
    send_len = str(msg_len).encode(format)
    send_len += b' '* (header - len(send_len))
    client.send(send_len)
    client.send(message)
    print(client.recv(2048).decode(format))

send(f"Client's IP address is {Server} and Client's device name is {socket.gethostname()}")
send(disconnect_message)
