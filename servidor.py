from xmlrpc.server import SimpleXMLRPCServer

def calcular_pontos(valor_compra, pontos_por_real):
    return valor_compra * pontos_por_real

servidor = SimpleXMLRPCServer(("localhost, 8004"))

servidor.register_function(
    calcular_pontos,
    "calcular_pontos"
)

print(" Servidor RPT aguardando solicitaçôes...")

servidor.serve_forever()
