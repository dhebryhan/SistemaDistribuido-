
from socket import *

serverPort = 9999
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('Funcionando')


while 1:
    connectionSocket, addr = serverSocket.accept()
    nomeArquivo = connectionSocket.recv(1024)
    try:
        arq = open(nomeArquivo.decode()+'.txt', 'r')
        for i in arq.readlines():
            connectionSocket.send(i.encode())
        arq.close()
    except Exception as e:
        print(e)
        connectionSocket.send("Arquivo nao existe".encode())
        
    connectionSocket.close()

 