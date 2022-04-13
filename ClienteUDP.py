import threading

from socket import *
serverName = '127.0.0.1'
serverPort = 9999
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect((serverName, serverPort))


def main(mensagem,cliente):
    mensagem = mensagem.split(",")
    
    try:
        for i in mensagem:
            
            clientSocket.send((str(i)+";"+cliente).encode())
            modifiedSentence = clientSocket.recv(1024)
            print("Vindo do servidor", modifiedSentence.decode())

    except Exception as e:        
        print(" ")
    

if __name__ == '__main__':
    aluno1 = threading.Thread(target=main, args=["1;4;VVFF,1;4;FFFV,1;5;VVVFV,1;4;VFFV,1;4;FVFV","Hecktor"])
    aluno2 = threading.Thread(target=main, args=["1;4;VFVF,1;4;FVVF,1;5;FFVFV,1;4;VFVV,1;4;FVFV","Heron"])
    aluno3 = threading.Thread(target=main, args=["1;4;FFFV,1;4;VFVV,1;5;VVFF,1;4;VVFV,1;4;FVFV","Kallebe"])
    
    aluno1.start()
    aluno2.start()
    aluno3.start()
