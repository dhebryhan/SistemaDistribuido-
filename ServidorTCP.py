from socket import *

portaServidor = 9999
servidorSocket = socket(AF_INET, SOCK_STREAM)
servidorSocket.bind(('', portaServidor)) #para qual porta deve esperar conexao.
servidorSocket.listen(5) #coloca o socket no modo servidor e limite de conexao.
print('Funcionando')


while 1:
    conexaoSocket, addr = servidorSocket.accept() #Deixa o servidor na escuta.
    nomeArquivo = conexaoSocket.recv(1024)
    try:
        arq = open(nomeArquivo.decode()+'.txt', 'r')
        for i in arq.readlines(): #retorna uma string no arquivo.
            conexaoSocket.send(i.encode())
        arq.close() #fecha o arquivo.
    except Exception as e:
        print(e)
        conexaoSocket.send("Arquivo nao existe".encode())
        
    conexaoSocket.close()

 
 
