lista = [[3, 4, 5], 
         [5,6, 9],
         [7,8, 2]]
#for s in lista:
#    print(*s)
'''
dia_s = []    
dia_p = []
for i in range(len(lista)):
    for k in range(len(lista)):
        if i == k:
            dia_p.append(lista[i][k])
        if i+k == len(lista)-1:
            dia_s.append(lista[i][k])
print(dia_s)     
print(dia_p)
'''
#print("Ingrese las 3 coordenadas en una simple fila (separados por espacio): ")
    # User input of entries in a 
    # single line separated by space
    #entries = list(map(float, input().split()))
    # For printing the matrix
    #matrix = np.array(entries).reshape(3, 2)
    #print(matrix)
    #col_1 = matrix[:,0]
    #col_2 = matrix[:,1]
    #'ok' if (col_1 <= 6.306).all() and (col_1 >= 5.888).all() else 'Error'
    #'ok' if (col_2 >= -72.321).all() and (col_2 <= -72.552).all() else 'Error Coordenada'
    #verif = float(input('Ingresa la coordenada que desea actualizar: '))
    #nueva_coord = float(input('Ingresa la nueva coordenada: '))
    #matrix[matrix == verif] = nueva_coord


#def main_matri(m):
#    cadena = '['
#    for i in range(len(m)):
#        for k in range(len(m[i])):
#            cadena += '{:>2s}'.format(str(m[i][k])) # remplazando variable #str >correr hacia la derecha 2s significa 2 espacios
 #       cadena = ']\n'
 #   return cadena

#print(main_matri(lista))


#def badmatrix(n,m):
#    a = [0]*m
#    matriz = [a]*n
#    return matriz

#M = badmatrix(2,3)
#print(M)

#%%
#lista = [[3, 4, 5], 
#         [5,6, 9],
#         [7,8, 2]]
#for s in lista:
#    print(*s)

#%%

#x = 'hola lindo'
#result = x.split(' ')
#print(result)
# %%
#l = [[1, 3, 4], [2, 5, 7]]
#print('\n'.join(' '.join(map(str,i)) for i in l))

#%%
#a = [[1, 3, 4], [2, 5, 7]]
#for i in a:
#    for j in i:
#        print(j, end = ' ')
#    print('',sep='\n')
# %%
#l = [[1, 3, 4], [2, 5, 7], [6, 9, 3], [1, 2, 8]]   
#[l[i:i+2] for i in range(0, len(l), 2)]

# %%

#matrix = [[1,2,3],[4,5,6],[7,8,9]]

#[[row[i] for row in matrix] for i in range(3)]


#%%
#lista = [[1, 2, 3],[50, 7, 8],[6, 4, 0]]
#print('\n'.join(' '.join(map(str,i)) for i in lista))

# %%
#lista = [[1, 2, 3, 10],[50, 7, 8, 1],[6, 44, 0, 9]]
#for i in lista:
#    for j in i:
#        print(j, end = '   ')
#    print('',sep='\n')
# %%
#x = [print(j, end = ' ') for j in i for i in lista]

# %%
#lista = [[1, 2, 3, 10],[50, 7, 8, 1],[6, 44, 0, 9]]
#for row in lista:
#    for val in row:
 #       print('{:4}'.format(val))
 #   print('', sep='\n')
# %% MATRIX ORDENADA
#lista = [[1, 2, 3, 10],[50, 7, 8, 1],[6, 44, 0, 9]]
#length_list = [len(str(element)) for row in lista for element in row] # Encuentra la long de los elementos en la columna
#columns_width = max(length_list) # Encuentra el elemento mas largo, el ancho de la columna
#for  row in lista:
#    row = ''.join(str(element).ljust(columns_width + 2) for element in row) # str.ljust se usa para la representacion de cada columna de la tabla como str
#    print(row)

#%% iterate through rows
'''
X = [[1,2,3,1],
    [4,5,6,1],
    [7,8,9,4],
    [6,3,2,2]]
  
Y = [[9,8,7,4],
    [6,5,4,9],
    [3,2,1,7],
    [4,7,8,9]]
for i in range(len(X)):  
# iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
 
#for r in result:
 #   print(r)
'''