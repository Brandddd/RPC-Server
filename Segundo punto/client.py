import xmlrpc.client

''' AUTORES: 
    BRANDON DAVID PALACIO ALVAREZ
    JORGE ALEXANDER OSORIO '''

proxy = xmlrpc.client.ServerProxy("http://localhost:8001/")
usuario = input('Ingrese el usuario: ')
clave = input('Ingrese la clave: ')

if (proxy.autenticar(usuario, clave)):
    menu = int(input("\nBienvenido.\nA ingresado satisfactoriamente al sistema: \n\n"
                     "1. Ingresar valores a la lista. \n"
                     "2. Retornar lista invertida. \n"
                     "3. Mostrar numero más repetido dentro de la lista. \n"
                     "4. Salir. \n\n"
                     "POR FAVOR, DIGITE UNA OPCION: "))
    while menu != 4:
        if menu == 1:
            dir = 'lista.txt'
            archivo = open(dir, 'w')

            for i in range(15):
                num = input(f'Ingrese el valor # {i+1}: ')
                archivo.write(f'{num} ')
            archivo.close()
            print("Lista de archivos creada satisfactoriamente. \n\n")

        elif menu == 2:
            print ('\nLa lista invertida es:\n', proxy.listaInvertida(dir))
        
        elif menu == 3:
            print ('\nEl número más repetido es: ', proxy.masRepetido(dir))

        elif menu == 4:
            print ('\nSaliendo... ')
            break

        else:
            ('\nPor favor digite una opcion correcta... ')

        menu = int(input("\nRETORNANDO A MENU PRINCIPAL: \n\n"
                     "1. Ingresar valores a la lista. \n"
                     "2. Retornar lista invertida. \n"
                     "3. Mostrar numero más repetido dentro de la lista. \n"
                     "4. Salir. \n\n"
                     "POR FAVOR, DIGITE UNA OPCION: "))   
else:
    print('Los datos ingresados son incorrectos')