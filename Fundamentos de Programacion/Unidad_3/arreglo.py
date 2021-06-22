#%% Leer arreglos de n datos de manera invertida
datos = []
num = int(input('Ingresa la cantidad de datos: '))
for i in range(1, num+1):
    datos.append(i)
print(datos[::-1])