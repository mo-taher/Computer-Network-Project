import socket # Importing socket library

header = 16 # How many bytes of data will be trasmitted
port = 5050 # Not a dedicate port address
Server = socket.gethostbyname(socket.gethostname()) # To fetch the devices IP address
addr = (Server, port) # Binding the IP address
format = "utf-8" # Format in which encoding and decoding will take place
disconnect_message = "End" # To show termination

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # We need these two things to transmit data from client to server
server.bind(addr) # To bind the socket address with the server object!

server.listen()
print("Server is listening")
conn, addr = server.accept()
connected = True

while connected:
    msg_len = conn.recv(header).decode(format)
    if msg_len:
        msg_len = int(msg_len)
        msg = conn.recv(msg_len).decode(format)

        if msg == disconnect_message:
            connected = False
            conn.send("Goodbye".encode(format))
        else:
            print(msg)
            conn.send("Message Received".encode(format))

conn.close()

