from socket import *

def main():
    serverPort = 9999
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))
    print("Servidor Funcionando")
    while 1:
        message, clientAddress = serverSocket.recvfrom(2048)
        message = message.decode().split(";")
        print("Envios do cliente", (message[3]+": "+message[0]+";"+message[1]+";"+message[2]).encode())
        z = 0
        w = 0
        for i in message[2]:
            
            if i == "F":
                w += 1
            if i == "V":
                z += 1

       

        modifiedMessage = (message[3]+": "+message[0]+";"+str(z)+";"+str(w)).encode()
        serverSocket.sendto(modifiedMessage, clientAddress)



if __name__ == '__main__':
    main()    #
