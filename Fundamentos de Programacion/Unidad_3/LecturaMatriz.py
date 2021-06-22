# %% MATRIX ORDENADA
lista = [[1, 2, 3, 10],[50, 7, 8, 1],[6, 44, 0, 9]]
length_list = [len(str(element)) for row in lista for element in row] # Encuentra la long de los elementos en la columna
columns_width = max(length_list) # Encuentra el elemento mas largo, el ancho de la columna
for  row in lista:
    row = ''.join(str(element).ljust(columns_width + 2) for element in row) # str.ljust se usa para la representacion de cada columna de la tabla como str
    print(row)
# %%
