from time import sleep
from socket import *
serverName = '127.0.0.1'
serverPort = 9999

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
arq = open('resultado.txt', 'w')
l = 0
sentence = input('Qual arquivo para baixar:')
clientSocket.send(sentence.encode())


while 1:
    dados = clientSocket.recv(1024)
    sleep(1)
    print("linha "+str(l)+": "+dados.decode())
    l += 1
    if not dados:
        break
    arq.write(dados.decode())
   
arq.close()

clientSocket.close()