import threading

from socket import *
serverName = '127.0.0.1'
serverPort = 9999
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect((serverName, serverPort))


def main(mensagem,cliente):
    mensagem = mensagem.split(",") #divisão de string
    
    try:
        for i in mensagem:
            
            clientSocket.send((str(i)+";"+cliente).encode())
            modifiedSentence = clientSocket.recv(1024) #ler caracteres de resposta de soquete em string
            print("Vindo do servidor", modifiedSentence.decode())

    except Exception as e:        
        print(" ")
    

if __name__ == '__main__':
    aluno1 = threading.Thread(target=main, args=["1;1;VVFF,1;2;FFFV,1;3;VVFFF,1;4;VFFV,1;5;FVFV","Hecktor"])
    aluno2 = threading.Thread(target=main, args=["1;1;VFVF,1;2;FVVF,1;3;FFVFV,1;4;VFVV,1;5;FVFV","Heron"])
    aluno3 = threading.Thread(target=main, args=["1;1;FFFV,1;2;VFVV,1;3;VVFF,1;4;VVFV,1;5;FVFV","Kallebe"])
    
    aluno1.start()
    aluno2.start()
    aluno3.start()
