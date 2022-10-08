import socket
import time

header = 16
port = 5050
server = socket.gethostbyname(socket.gethostname())
addr = (server,port)
format = 'utf-8'
disconnect_message = 'end'
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)
server.listen()
print("Server is Running\n")
conn, addr = server.accept()

while True:
    msg_length = conn.recv(header).decode(format)
    if not msg_length: break

    msg_length = int(msg_length)
    msg = conn.recv(msg_length).decode(format)

    if msg == disconnect_message:
        conn.send('\nServer Stopped'.encode(format))
        break

    hours = int(msg)
    salary = 0
    print('Hours Worked:', hours)

    if (hours == 0):
        salaryResponse = 'Salary: 0 Taka\n'
        conn.send(salaryResponse.encode(format))
    elif (hours <= 40):
        salary = str(hours * 200)
        salaryResponse = 'Salary: ' + salary + ' Taka\n'                    
        conn.send(salaryResponse.encode(format))
    elif (hours > 40):
        salary = salary + 8000
        extraHours = hours - 40
        extraSalary = extraHours * 300
        salary = str(salary + extraSalary)
        salaryResponse='salary: ' + salary + 'Taka\n'          
        conn.send(salaryResponse.encode(format))    

    time.sleep(0.5)

conn.close()