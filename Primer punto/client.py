import xmlrpc.client

''' AUTORES: 
    BRANDON DAVID PALACIO ALVAREZ
    JORGE ALEXANDER OSORIO '''

dir = 'lista.txt'
archivo = open(dir, 'w')

for i in range(15):
    num = input(f'Ingrese el valor # {i+1}: ')
    archivo.write(f'{num} ')
archivo.close()

proxy = xmlrpc.client.ServerProxy("http://localhost:8001/")
print ('La lista invertida es:\n', proxy.listaInvertida(dir))
print ('El número más repetido es: ', proxy.masRepetido(dir))