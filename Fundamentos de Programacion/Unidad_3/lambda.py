anonima = lambda x, y: x + y

valor = anonima(6, 3)
print(valor)
lista = [50, 45, 53, 21]
lista2 = [3, 6, 5, 7]
listasuma = list(map(anonima, lista, lista2))
print(listasuma)
filtrar = list(filter(lambda x : x > 50, lista))
print(filtrar)

#%%
# lista que imprime los valores mayore o menores al promedio de esa lista
lista = [50, 45, 75, 80, 97, 34]
promedio = (sum(lista))/len(lista)
val_mayores = list(filter(lambda x : x > int(promedio), lista))
val_menores = list(filter(lambda x : x < int(promedio), lista))
print(val_mayores, val_menores)

#%%
cadena = 'holamundo1234'
res = "".join(filter(lambda x: not x.isdigit(), cadena))
print(res)

#%%
cadena = 'holamundo1234'
result = ''.join([i for i in cadena if not i.isdigit()])
print(result)
