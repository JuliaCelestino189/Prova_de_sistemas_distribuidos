from xmlrpc.server import SimpleXMLRPCServer

def calcular_pontos(valor_compra, pontos_por_real):
    return valor_compra * pontos_por_real

servidor = SimpleXMLRPCServer(("localhost, 8004"))

servidor = SimpleXMLRPCServer(
    ("localhost", 8000),
    allow_none=True
)


print(" Servidor RPT aguardando solicitaçôes...")

servidor.serve_forever()


PS C:\Users\Julia\OneDrive\Documentos\Prova-de-sistemas-distribuidos> & C:/Users/Julia/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/Julia/OneDrive/Documentos/Prova-de-sistemas-distribuidos/servidor.py
 Servidor RPT aguardando solicitaçôes...
