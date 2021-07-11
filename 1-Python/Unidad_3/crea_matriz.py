import math        
with open('crea_matriz.txt', 'r+') as f:
    for i in f.readlines():
        fila = i.split(',')
        tamaño_fila = len(fila)
        x = int(math.sqrt(tamaño_fila))
        list_of_lists = [fila[j:j+x] for j in range(0, len(fila), x)] # range (start, stop, step)
        print(list_of_lists)