def no_duplicate(cedula):
    with open('menu.txt', 'r+') as f:
        for i in f.readlines():
            if cedula in i:
                print('Cedula ya existe')
                break
            
while True:
    menu = int(input('''
    1. Escribir
    2. Cambiar cedula
    3. Salir
    :'''))
    if menu == 1:       
        with open('menu.txt', 'a') as f:
            campos = ['cedula', 'nombre', 'apellidos', 'direccion']
            for val in campos:
                a = input(f'Ingrese la informacion de {val}: ')
                f.write(a + '|') 
            f.write('\n') 
        
    elif menu == 2:
        search_cedula = input('Ingrese la cedula a buscar: ')
        new_cedula = input('Ingresa la nueva cedula: ')
        with open("menu.txt", "r+") as fin:
            with open("out.txt", "w+") as fout:
                for line in fin:
                    fout.write(line.replace(str(search_cedula), str(new_cedula)))
    elif menu == 3:
        break
    else:
        print('Ingresa un num de 1-3')


