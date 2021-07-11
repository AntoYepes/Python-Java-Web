#%% CICLOS
# Ciclo while
cont = 0
acum = 0
n = 10
while n > 0:
    cont += 1
    acum += cont 
    n -= 1
print(cont)
print(acum)

#%%
# No 6, 28 numero perfecto:
# sumo sus divisores 1+2+3 = 6
# sumo sus divisores 1+2+7+4+14 = 28
# dado un no entero me diga si es perfecto o no es perfecto

num_ingresado= int(input('Ingrese el numero para verificar:'))
num = 1
suma = 0

while num < num_ingresado:
    if num_ingresado % num == 0:
        suma += num
    num += 1

if suma == num_ingresado:
    print('El numero es perfecto')
else:
    print('El numero no es perfecto')


# %%
# Numero primo: divisores 1 y el mismo
numero = int(input('Ingrese un numero: '))
div = 2
bandera = True

while div < numero:
    if numero % div == 0:
        bandera = False
        break
    div += 1 # El div va aumentando 2, 3, 4
if bandera:
    print(f'El numero {numero} es primo')
else:
    print(f'El numero {numero} NO es primo')
    


# %%
