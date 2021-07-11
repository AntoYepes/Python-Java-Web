bandera = True
lista = ["que","hambre","tengo","sorry","por avanzar"]
while bandera == True:
    
    print(lista)
    x = int(input("Ingrese un numero: "))
    salvar = lista[x-1]
    lista.pop(x-1)
    nlista = [salvar] + lista
    #lista = nlista
    print(lista)
    print(nlista)
    if x == False:
        bandera = False