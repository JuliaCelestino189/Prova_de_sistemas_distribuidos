from xmlrpc.client import ServerProxy

servidor = ServerProxy("http://localhost:8004/")
resultado = servidor.calcular_ponto(120,2)

print("Pontos recebidos: ", resultado)
