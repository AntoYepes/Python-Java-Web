#%% Menu con while
import os
import time

while True:
    num_1 = int(input('Ingresa el primer numero: '))
    num_2 = int(input('Ingresa el segundo numero: '))
    try:
        opc = int(input('''
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Salir
        :'''))
        if opc == 1:
            print(num_1 + num_2)
        elif opc == 2:
            print(num_1 - num_2)
        elif opc == 3:
            print(num_1 * num_2)
        elif opc == 4:
            print(num_1 / num_2)
        elif opc == 5:
            break
        else:
            print('Opcion incorrecta, vuelve a intentarlo!')
        time.sleep(1)
        os.system('cls')
    except:
        print('Ingrese solo un numero: ')
        
# %%
