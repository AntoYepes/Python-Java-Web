#%%
# Funciones incorporadas
num = int('32')
num_float = float('32.5')
cadena = str(32)
print(num, num_float, cadena)

# len , min, max
print(len('hola lindo'))
print(min([5,6,7,8,9,0]))
print(max([1,2,3,4,5,6,7,8]))

#%% Importando librerias
import math
print(math.sqrt(5))

#%% Funcion como randomint
import random
import os
def aleatory_num(start, end):
    num = int(start + random.random() * end)
    return num

guess = aleatory_num(1, 20)
cont = 0
while True:
    num_ing = int(input('Ingrese un valor entre 1-20: '))
    if num_ing == guess:
        cont += 1
        print(f'Ganaste con {cont} intentos')
        resp = input('¿Deseas seguir jugando?: si/no ')
        cont = 0
        if resp == 'si':
            guess = aleatory_num(1, 20)
            continue
        elif resp == 'no':
            break
        else:
            print('Respuesta invalida')
    else:
        cont += 1
        print(f'Fallaste llevas {cont} intentos, intentalo nuevamente!')
        if num_ing > guess:
            print('Ingresaste un valor por encima ')
        else:
            print('Ingresaste valor por debajo')
        
# %%