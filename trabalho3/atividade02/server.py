import Pyro4

class Server(object):
    @Pyro4.expose
    def welcomeMessage(self, name):
        verdadeira = 0
        falso = 0
        questao = name.split(";") 
        alt = questao[2] 

        for x in alt: 
            if((x == "V") or (x == "v")):
                verdadeira = verdadeira + 1
            if((x == "F") or (x == "f")):
                falso = falso + 1    

        res = questao[0], " Possui ", verdadeira, " Verdadeira ", falso, " Falsa"
        return  res

def startServer():
    server = Server()
    daemon = Pyro4.Daemon()             
    ns = Pyro4.locateNS()
    uri = daemon.register(server)  
    ns.register("server", uri)   
    print("Ready. Object uri =", uri)
    daemon.requestLoop()                   

if __name__ == "__main__":
    startServer()