from socket import *
from time import ctime

HOST = 'localhost'
PORT = 8080
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(100)

while True:
    print('wating for connect ...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('... connect from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        tcpCliSock.send('[%s] %s' % (bytes(ctime(), 'utf-8'), data))
        tcpCliSock.close()

    tcpSerSock.close()