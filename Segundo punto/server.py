from xmlrpc.server import SimpleXMLRPCServer

''' AUTORES: 
    BRANDON DAVID PALACIO ALVAREZ
    JORGE ALEXANDER OSORIO '''

datosUsuario = ('falcao', 'rayo2022')

def verificarUsuario(usuario, clave):
    if (usuario, clave) == datosUsuario:
        return True
    else:
        return False

def invertirLista(dir):
    archivo = open(dir, 'r')
    listaInvertida = []
    lista = []
    cadena = archivo.read()
    num = ''

    for letra in cadena:
        if letra == ' ':
            lista.append(num)
            num = ''
        else:
            num += letra

    for i in range(14, -1, -1):
        listaInvertida.append(lista[i])

    return listaInvertida

def repetidoLista(dir):
    archivo = open(dir, 'r')
    lista = []
    repetidos = {}
    cadena = archivo.read()
    num = ''

    for letra in cadena:
        if letra == ' ':
            lista.append(num)
            num = ''
        else:
            num += letra

    for i in lista:
        if i in repetidos.keys():
            repetidos[i] += 1
        else:
            repetidos[i] = 0

    numMasRepetido = lista[0]
    for llave, valor in repetidos.items():
        if valor > repetidos[numMasRepetido]:
            numMasRepetido = llave
            
    return numMasRepetido

server = SimpleXMLRPCServer(("localhost", 8001))
server.register_function(verificarUsuario, "autenticar")
server.register_function(invertirLista, "listaInvertida")
server.register_function(repetidoLista, "masRepetido")
print ("Servidor ejecutandose en el puerto 8001")
server.serve_forever()