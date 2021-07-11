#%%
def df_matrix_table(lista):
    length_list = [len(str(element)) for row in lista for element in row] # Encuentra la long de los elementos en la columna
    columns_width = max(length_list) # Encuentra el elemento mas largo, el ancho de la columna
    for  row in lista:
        row = ''.join(str(element).ljust(columns_width + 2) for element in row) # str.ljust se usa para la representacion de cada columna de la tabla como str
        print(row)
        
X = [[1,2,3,1],
    [4,5,6,1],
    [7,8,9,4],
    [6,3,2,2]]
  
Y = [[9,8,7,4],
    [6,5,4,9],
    [3,2,1,7],
    [4,7,8,9]]
#len(x[0]) es la cantidad de cada sublista
suma = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]
resta = [[X[i][j] - Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]
multp = [[X[i][j] * Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

df_matrix_table(suma)
df_matrix_table(resta)
df_matrix_table(multp)
# %%
