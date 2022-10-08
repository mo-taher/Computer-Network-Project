import socket
import time, threading
from wsgiref.simple_server import server_version

header = 16
port = 5050
server = socket.gethostbyname(socket.gethostname())
addr = (server,port)
format = 'utf-8'
disconnect_message = 'end'
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)
   
def server_running(conn, addr):
    
    
    while True:
        msg_length = conn.recv(header).decode(format)
        if not msg_length: break
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(format)

        if msg == disconnect_message:
            conn.send('\nServer Stopped'.encode(format))
            break

        count = 0
        print('Message:', msg)
        for char in msg:
            if (char in 'AEIOUaeiou'):
                count = count + 1
        
        if (count == 2):
            conn.send('Enough vowels I guess\n'.encode(format))
        elif (count > 2):
            conn.send('Too many vowels\n'.encode(format))
        else:
            conn.send('Not enough vowels\n'.encode(format))
        
        time.sleep(1)

    conn.close()

server.listen()
print("Server is Running")

while True:
    conn, Addr = server.accept()
    thread = threading.Thread(target=server_running, args=(conn,addr))
    thread.start()
