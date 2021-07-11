
# %% PRUEBAS

datos = []	
for i in ["casa","trabajo","parque"]:
    lista = []
    for k in  ["latitud","longitud"]:
        x = input(f'Ingrese la {k} de {i}')
        lista.append(x)
    datos.append(lista)
coord_casa = datos[0]
coord_trabajo = datos[1]
coord_parque = datos[2]	

print(datos)
print(coord_casa)
print(coord_trabajo)
print(coord_parque)
# %%
# Lista para emular el contenido de tu csv
f = ['"4","8","9"\n',
     '"8","6","6"\n',
     '"8","6","1"\n']

pos = 2
columna = [int(line.replace('"','').rstrip('\n').split(",")[pos]) for line in  f]
print(columna)
# [9, 6, 1]

# %%
data = [['a','b'], ['a','c'], ['b','d']]
search = 'c'
any(e[1] == search for e in data)
# %%
data = [['a','b'], ['a','c'], ['b','d']]
search = 'c'
for sublist in data:
    if sublist[1] == search:
        print (sublist)
        break
# %%
a_list = [3, 2, 1]
min_value = min(a_list)
min_index = a_list.index(min_value)
print(min_index)
# %%
verif_min = [1436, 767, 1418, 1363]
def min_values(lista):
    m1 = min(verif_min)
    indx1 = lista.index(m1)
    m2 = min(v for v in verif_min if v != m1) 
    indx2 = lista.index(m2)
    return indx1, indx2
min_values(verif_min)

#%%
