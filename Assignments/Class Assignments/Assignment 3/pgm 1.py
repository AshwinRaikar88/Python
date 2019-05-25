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
