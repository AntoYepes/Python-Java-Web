# %% PRACTICA No 1

a = int(input('Ingrese el valor de a:'))
b = int(input('Ingrese el valor de b: '))
c = int(input('Ingrese el valor de c:'))

lista = sorted([a, b, c])
print('El numero menor es: ', lista[0])
print('El numero del medio es: ', lista[1])
print('El numero mayor es: ', lista[2])
# %%
a = int(input('Ingrese el valor de a:'))
b = int(input('Ingrese el valor de b: '))
c = int(input('Ingrese el valor de c:'))

# Verificar 
if a < b and a < c:
    print('a es el menor')
    if b < c:
        print('b es el del medio')
        print('c es el mayor')
    else:
        print('c es el del medio')
        print('b es el mayor')
if b < a and b < c:
    print('b es el menor')
    if a < c:
        print('a es el del medio')
        print('c es el mayor')
    else:
        print('c es el del medio')
        print('a es el mayor')
if c < a and c < b:
    print('c es el menor')
    if a < b:
        print('a es el del medio')
        print('b es el mayor')
    else:
        print('b es el del medio')
        print('a es el mayo')

# %%
entero = input('Ingrese un numero:')
try:
    numero = int(entero)
    if numero > 0:
        print('El numero es positivo')
    else:
        print('El numero es negativo')
except:
    print('Debe ingresar un numero')
