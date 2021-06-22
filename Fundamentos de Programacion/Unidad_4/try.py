import math

# Funcion que encuentra los 2 valores min con indices
def min_values(lista):
    m1 = min(lista)
    indx1 = lista.index(m1)
    m2 = min(v for v in lista if v != m1) 
    indx2 = lista.index(m2)
    return [m1, m2, indx1, indx2]

# Funcion que calcula la distancia con la coord actual
def get_distance(coordenada, matriz):
    coord = coordenada # toma el valor de la coordenada que el usuario escoja
    # punto 1 coord
    lat1 = coord[0] # latitud punto1
    lon1 = coord[1] # long punto 1
    # punto 2 cada coso del matrix
    list_distc = []
    for i in matriz:
        lat2 = i[0]
        lon2 = i[1]
        d_lat = round(lat2 - lat1, 3)
        d_lon = round(lon2 - lon1, 3)  
        r_tierra = 6372.795
        distance = 2 * r_tierra * math.sin(math.sqrt((math.pow(math.sin(d_lat/2), 2))+(math.cos(lat1))*(math.cos(lat2))*(math.pow(math.sin(d_lon/2), 2))))
        list_distc.append(int(distance))
    need_indx = min_values(list_distc) # lista donde tengo los valores minimos y los indices de las 2 distancias menores
    # Comparar usuarios
    users_1 = matriz[need_indx[2]][2]
    users_2 = matriz[need_indx[3]][2]
    if users_1 <= users_2:
        flag = [0, 1]
        user1 = users_1
        user2 = users_2
    else:
        flag = [1, 0]
        user1 = users_2 
        user2 = users_1
    print(f'La zona wifi 1: ubicada en {coord} a {need_indx[flag[0]]} metros tiene en promedio {user1}')
    print(f'La zona wifi 2: ubicada en {coord} a {need_indx[flag[1]]} metros tiene en promedio {user2}')
    choose = int(input(('Elija 1 o 2 para recibir indicaciones de llegada')))
    if choose == 1:
        bandera = 2
    elif choose == 2:
        bandera = 3
    else:
        print('Error zona wifi')
        exit()
    # latitud y long de las distancias menores
    lat1_c = matriz[need_indx[bandera]][0]
    lon1_c = matriz[need_indx[bandera]][1]
    
    address_lat = lat1 - lat1_c
    if address_lat < 0:
        lat_result = 'norte'
    else:
        lat_result = 'sur'
    address_lon = lon1 - lon1_c
    if address_lon < 0:
        lon_result = 'este'
    else:
        lon_result = 'oeste'
    print(f'Para llegar a la zona wifi dirigirse primero al {lon_result} y luego hacia el {lat_result}')
        
    vel_pie = 0.483
    vel_bici = 3.33
    tiempo_pie = print('Tiempo a pie: ', int(need_indx[flag[0]]/vel_pie), 'segundos')
    tiempo_bici = print('Tiempo en bicicleta: ', int(need_indx[flag[0]]/vel_bici), 'segundos')
        
        
matrix = [[6.211, -72.482, 2], 
        [6.212, -72.470, 25], 
        [6.105, -72.342, 25], 
        [6.210, -72.442, 50]]
coord = [6.301, -72.501] 
get_distance(coord, matrix)