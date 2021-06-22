#%% CICLO ANIDADO
for i in range(1,6): # de 1 a 5
    for j in range(1,4):
        print(f'El valor de i es {i}, y el valor de j es {j}')
        
#%% No PRIMOS
num = int(input('Ingrese la cant de numeros primos a generar: '))
cont = 0
numero = 2
while cont < num:
    counter = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            counter += 1
    if counter == 2:
        cont += 1
        print(f'Numero primo {numero}')
    numero += 1
print('Fin del programa')    
    
# %%
