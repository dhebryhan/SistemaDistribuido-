from time import sleep #atraso de tempo
from socket import * #
nomeServidor = '127.0.0.1'
portaServidor = 9999

s = socket(AF_INET, SOCK_STREAM) #AF_inet -> tipo de Ip ; sock_stream -> definindo socket de fluxo.
s.connect((nomeServidor, portaServidor)) #método de conexao
arquivo = open('resultado.txt', 'w') #open metodo para leitura e escrita de documento.
l = 0
nomeDocumento = input('Qual arquivo para baixar:') 
s.send(nomeDocumento.encode()) #


while 1:
    dados = s.recv(1024) #esperando terminar trocas de mensagens
    sleep(1)
    print("linha "+str(l)+": "+dados.decode()) #decode melhora a visualização das resposta
    l += 1
    if not dados:
        break
    arquivo.write(dados.decode())
   
arquivo.close()

s.close()#fechar conexao.
