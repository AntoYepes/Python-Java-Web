import os,time
path = os.getcwd()+'/test/datos.txt'

def menu():
    print('1. Ingresar datos contacto')
    print('2. Buscar')
    print('3. Actualizar')
    print('4. Eliminar')
    print('5. Salir')

def entradaDato():
    cedula=input('Ingrese Cédula: ')
    nombre=input('Ingrese Nombre: ')
    apellidos=input('Ingrese Apellidos: ')
    direccion=input('Ingrese Dirección: ')
    return cedula,nombre,apellidos,direccion

def insertarDatos(cedula,nombre,apellidos,direccion):
    with open(path,'a') as file_data:
        existentes=buscar(cedula)
        if len(existentes)==0:
            tupla = cedula,nombre,apellidos,direccion
            datos = ';'.join(tupla)
            file_data.write(datos+'\n')
        else:
            raise Exception(f'Contacto con cédula {cedula} ya existe ')

def buscar(cedula):
    lista_vacia=list()
    with open(path) as file_data:
        for linea in file_data.readlines():
            lista_datos=linea.split(';')
            if cedula in lista_datos:
                return lista_datos
        return lista_vacia

menu()
while True:
    op = input('Ingrese una opción entre 1 y 5 ')
    if op == '1':
        try:
            cedula,nombre,apellidos,direccion=entradaDato()
            insertarDatos(cedula, nombre, apellidos, direccion)
            print('Datos ingresados correctamente..')
            time.sleep(5)
            os.system('clear')
            menu()
        except Exception as error:
            print('Error',error)
            time.sleep(5)
            os.system('clear')
            menu()
    elif op == '2':
        cedula = input('Ingrese cédula ')
        contacto=buscar(cedula)
        if len(contacto) != 0:
            print('Cedula: {0}{4} Nombre:{1}{4} Apellidos: {2}{4} Dirección:{3}'.format(contacto[0],contacto[1],contacto[2],contacto[3],' | '))
            time.sleep(5)
            os.system('clear')
            menu()
        else:
            print('Registro no encontrado')
    elif op == '5':
        break
        print('Fin del programa...')