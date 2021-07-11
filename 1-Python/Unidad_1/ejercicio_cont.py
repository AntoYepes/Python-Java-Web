import time
import os
password = 'python'
cont = 0
while True:
    contraseña = input(('Ingrese el password: '))
    if password != contraseña.lower():
        cont += 1
        if cont == 4:
            time.sleep(5)
        os.system('cls')
    else:
        print('Ingreso exitoso')
        break
    
            