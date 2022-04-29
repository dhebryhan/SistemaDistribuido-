import Pyro4

name = input("Digite suas respostas ").strip()
server = Pyro4.Proxy("PYRONAME:server")
print(server.welcomeMessage(name))