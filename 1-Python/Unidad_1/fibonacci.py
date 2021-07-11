n = int(input('Ingrese el numero: '))
anterior = 0
siguiente = 1
cont = 1
while cont <= n:
    print(anterior, end='')
    anterior, siguiente = siguiente, anterior + siguiente
    cont += 1