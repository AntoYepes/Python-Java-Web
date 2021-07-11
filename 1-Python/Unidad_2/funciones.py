#%% FUNCIONES
# ¿Que es una funcion?
def nombre_func(param1, param2, param3, param4):
    pass

def menu():
    opc = input('''
    1. Opcion 1
    2. Opcion 2
    3. Opcion 3
    4. Salir
    :''')
    print(int(opc))
  
menu()
#%%    
def sumar(n1, n2):
    resultado = n1 + n2 
    print(resultado)
    
sumar(2, 3) # Invocar en el orden de los parametros
sumar(n1=6, n2=8) # invocar con parametros posicionales
datos = [100, 4]
print(sumar(*datos)) # desempaquetar
datos2 = {'n2': 250, 'n1':100}
print(sumar(**datos2)) # doble asterisco por ser diccionario
#%%
def restar(n1, n2=0):
    result = n1 - n2
    print(result)
    
restar(7) # Cuando hay valor por defecto
# %% multiples parametros *
def multiple(paramfijo, *parammultiple):
    print(paramfijo)
    for i in parammultiple:
        if type(i) == bool:
            print('Es un booleano')
        
multiple('Hola', 3,4,5,6,7,8,'U', True, 'I', 'Mensaje')

# %%
def sumamultiple(*n):
    suma = 0
    for i in n:
        suma += i
    print(suma)
    
sumamultiple(2, 3, 6)
# %% Cuatro operaciones +- / *
def sumar(n1, n2):
    resultado = n1 + n2 
    print(resultado)
    
def restar(n1, n2=0):
    result = n1 - n2
    print(result)
    
def multiplicar(n1, n2):
    answer = n1 * n2
    print(answer)
    
def division(n1, n2):
    answer = n1 / n2
    print(answer)
    
while True:
    opc = int(input('''
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Salir
    :'''))
    if opc == 1:
        n1 = int(input('Ingresa el 1er num: '))
        n2 = int(input('Ingresa el 2nd num: '))
        sumar(n1, n2)
    elif opc == 2:
        n1 = int(input('Ingresa el 1er num: '))
        n2 = int(input('Ingresa el 2nd num: '))
        restar(n1, n2)
    elif opc == 3:
        n1 = int(input('Ingresa el 1er num: '))
        n2 = int(input('Ingresa el 2nd num: '))
        multiplicar(n1, n2)
    elif opc == 4:
        n1 = int(input('Ingresa el 1er num: '))
        n2 = int(input('Ingresa el 2nd num: '))
        division(n1, n2)
    elif opc == 5:
        break
    else:
        print('Opcion invalida, ingrese num del 1-5: ')
# %%
