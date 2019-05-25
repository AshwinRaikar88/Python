'''1. Write the socket program so that it counts the number of characters it has
received and stops displaying any text after it has shown 3000 characters. The
program should retrieve the entire document and count the total number of
characters and display the count of the number of characters at the end of the
document.'''

import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect((HOST, PORT))
cmd = 'GET /code/mbox.txt HTTP/1.0\r\nHost: www.py4inf.com\r\n\r\n'.encode()
mysock.sendall(cmd)
count = 0

while True:
    data = mysock.recv(3000)
    if len(data) < 1: break
    time.sleep(0.005)
    count = count + len(data)
    print(len(data), count)

print ("\n\nTotal characters received= ",count)
mysock.close()
