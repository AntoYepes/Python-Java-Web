#%%
import math

def read_matrix(lista):
    length_list = [len(str(element)) for row in lista for element in row] # Encuentra la long de los elementos en la columna
    columns_width = max(length_list) # Encuentra el elemento mas largo, el ancho de la columna
    for  row in lista:
        row = ''.join(str(element).ljust(columns_width + 2) for element in row) # str.ljust se usa para la representacion de cada columna de la tabla como str
        print(row)

def verif(info):
    for i in info:
        if len(i) != (3 or 2):
            print('Error')
            prueba = 0
            break
        else:
            if (i[0] < 6.306 and i[0] > 5.888) and (i[1] < -72.321 and i[1] > -72.552):
                prueba = 1
                continue
            else: 
                print('Error coordenada')
                prueba = 0
                exit()
    return prueba 
            
        
matrix = [[6.211, -72.482, 2], [6.212, -72.470, 25], [6.105, -72.342, 25], [6.210, -72.442, 50]]
result = verif(matrix)
if result == 1:
    read_matrix(matrix)
else:
    exit()

while True:
    menu = int(input('''
    2. Ingresar coordenadas actuales
    3. Ubicar zona wifi más cercana
    :'''))
    if menu == 2:
        coord_trabajo = list(map(float, input("Ingresa las coordenadas del trabajo separada por espacios ").strip().split()))
        coord_casa = list(map(float, input("Ingresa las coordenadas de la casa separada por espacios ").strip().split()))
        coord_parque = list(map(float, input("Ingresa las coordenadas del parque separada por espacios ").strip().split()))
        datos = []
        datos.append(coord_trabajo)
        datos.append(coord_casa)
        datos.append(coord_parque)
        
        result = verif(datos)
        if result == 1:
            # Calculo para el valor mas cercano al oriente
            given_value = -72.321 
            flattened = [val for sublist in datos for val in sublist]
            absolute_difference_function = lambda list_value : abs(list_value - given_value)
            closest_value = min(flattened, key=absolute_difference_function)
            i=0
            new_list=[]
            while i<len(flattened):
                new_list.append(flattened[i:i+2])
                i+=2
            indx = [ele for i, ele in new_list].index(closest_value)
            coord = indx+1   

            # Calculo para el promedio de todos los puntos
            promd_lat = (coord_trabajo[0] + coord_casa[0] + coord_parque[0]) / 3
            promd_long = (coord_trabajo[1] + coord_casa[1] + coord_parque[1]) / 3
            compare_list = [promd_lat, promd_long]
                        
            # Se muestran los datos al usuario
            print(f'coordenada [latitud, longitud] 1 : {coord_trabajo}')
            print(f'coordenada [latitud, longitud] 2 : {coord_casa}')
            print(f'coordenada [latitud, longitud] 3 : {coord_parque}')
            print(f'La coordenada {coord} es la que está más al oriente')
            print(f'La coordenada {compare_list} es la promedio de todos los puntos')
            
            while True:
                opc_3 = int(input('Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú'))
                if opc_3 == 1:
                    coord_new = list(map(float, input("Ingresa las coordenadas del trabajo separada por espacios ").strip().split()))
                    datos[0] = coord_new
                    result = verif(datos)
                    if result == 1:
                        break
                    else:
                        exit()
                    
                elif opc_3 == 2:
                    coord_new = list(map(float, input("Ingresa las coordenadas del trabajo separada por espacios ").strip().split()))
                    datos[1] = coord_new
                    result = verif(datos)
                    if result == 1:
                        break
                    else:
                        exit()
                elif opc_3 == 3:
                    coord_new = list(map(float, input("Ingresa las coordenadas del trabajo separada por espacios ").strip().split()))
                    datos[2] = coord_new
                    result = verif(datos)
                    if result == 1:
                        break
                    else:
                        exit()
                elif opc_3 == 0:
                    break
                else:
                    print('Error actualización')
                    exit()    
        else:
            exit()    
    if menu == 3:
        if len(datos) == 0:
            print('Error sin registro de coordenadas')
            exit()
        else:
            while True:
                print(f'coordenada [latitud, longitud] 1 : {coord_trabajo}')
                print(f'coordenada [latitud, longitud] 2 : {coord_casa}')
                print(f'coordenada [latitud, longitud] 3 : {coord_parque}')
                opcion = int(input(('Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión')))
                if opcion == 1:
                    pass
                elif opcion == 2:
                    pass
                elif opcion == 3:
                    pass
                else:
                    print('Error ubicación')
                    exit()
            
# %%
import math    
matrix = [[6.211, -72.482, 2], [6.212, -72.470, 25], [6.105, -72.342, 25], [6.210, -72.442, 50]]
coord = [5.999, -72.401]
# punto 1 coord
lat1 = coord[0] # latitud punto1
lon1 = coord[1] # long punto 1
# punto 2 cada coso del matrix
for i in matrix:
    lat2 = i[0]
    lon2 = i[1]
    d_lat = round(lat2 - lat1, 3)
    d_lon = round(lon2 - lon1, 3)  
    r_tierra = 6372.795
    x = math.pow(math.sin(d_lat/2), 2)
    y = math.cos(lat1)
    z = math.cos(lat2)
    w = math.pow(math.sin(d_lon/2), 2)
    ecuacion = 2 * r_tierra * math.sin(math.sqrt(x+y*z*w))
    distancias = round(ecuacion, 3)
    print(distancias)
    #res_min = min(distancias,key=lambda x:float(x))
    #print(res_min)
    
# %%
