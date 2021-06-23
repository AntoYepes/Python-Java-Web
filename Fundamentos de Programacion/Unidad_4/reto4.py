# %%
import os
import time
import math

# Funcion para verificar los limites y la long de cada entrada
def verif(info):
    if type(info) == list:        
        for i in info:
            if len(i) != 2:
                print('Error2')
                prueba = 0
                exit()
            else:
                if (i[0] < 6.306 and i[0] > 5.888) and (i[1] < -72.321 and i[1] > -72.552):
                    prueba = 1
                    continue
                else: 
                    print('Error coordenada')
                    prueba = 0
                    exit()
        return prueba
    elif type(info) == str:
        try:
            x = float(info)
            
        except:
            print('Error')
            exit()
        if (x < 6.306 and x > 5.888) or (x < -72.321 and x > -72.552):
            return(x)
        else:
            print('Error coordenada')
            exit()

# Funcion que encuentra los 2 valores min con indices
def min_values(lista):
    m1 = min(lista)
    indx1 = lista.index(m1)
    m2 = min(v for v in lista if v != m1) 
    indx2 = lista.index(m2)
    return [m1, m2, indx1, indx2]

# Funcion que calcula la distancia con la coord actual
def get_distance(coordenada, matriz, flag2 = 0):
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
    
    if flag2 == 1:
        return matriz[need_indx[2]]
    
    if users_1 <= users_2:
        flag = [0, 1]
        u1 = users_1
        u2 = users_2
    else:
        flag = [1, 0]
        u1 = users_2 
        u2 = users_1 
        
    if flag2 == 0:    
        print(f'La zona wifi 1: ubicada en {coord} a {need_indx[flag[0]]} metros , tiene en promedio {u1} usuarios')
        print(f'La zona wifi 2: ubicada en {coord} a {need_indx[flag[1]]} metros , tiene en promedio {u2} usuarios')
    try:
        choose = int(input(('Elija 1 o 2 para recibir indicaciones de llegada')))
    except:
        print('Error zona wifi')
        exit()
    if choose == 1:
        bandera = 2
    elif choose == 2:
        bandera = 3
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
    tiempo_bici = print('Tiempo en bici: ', int(need_indx[flag[0]]/vel_bici), 'segundos')
    
datos = []
password = 1
# Mensaje de bienvenida
print('Bienvenido al sistema de ubicación para zonas públicas WIFI')
time.sleep(1) 
os.system('cls')
# Pedimos por consola el usuario
usuario = input('Ingrese el usuario: ')
if int(usuario) == 2: # Se verifica el usuario
    contraseña = int(input('Ingrese la contraseña: ')) # Se verifica la contraseña
    if contraseña == password: # Se verifica la contraseña
        num_1 = 638 # Primer No
        num_2 = (3*5-9-3 or  10 % 3 + 2) or ((10 // 2) - 2) # Segundo No
        captcha = input(f'Resuelva la suma {num_1} + {num_2} = ') # Captcha, la suma para comprobar si el inicio de sesion corresponde a un usuario
        if int(captcha) == 641:
            print('Sesión iniciada') # Si la suma es correcta sale sesion iniciada
            menu = ['1 Cambiar contraseña\n', '2 Ingresar coordenadas actuales\n', '3 Ubicar zona wifi más cercana\n', '4 Guardar archivo con ubicación cercana\n', '5 Actualizar registros de zonas wifi desde archivo\n','6 Elegir opción de menú favorita\n', '7 Cerrar sesión']
            contador = 0
            while True:
                print(*menu)
                opc = int(input('Elija una opción '))
                # Opcion No 1
                if opc == 1:
                    contraseña = int(input('Ingrese la contraseña actual: ')) # Se verifica la contraseña
                    if contraseña == password:
                        new_contraseña = int(input('Ingresa la nueva contraseña: '))
                        password = new_contraseña 
                        continue     
                    else:
                        print('Error')
                        exit()
                # Opcion No 2
                elif opc == 2:
                    if datos == []:                        
                        for i in range(3):
                            sublist = []
                            latitud = input('Latitud: ')
                            latitud = verif(latitud)
                            longitud = input('Longitud: ')
                            longitud = verif(longitud)
                            sublist.append(latitud)
                            sublist.append(longitud)
                            datos.append(sublist)
                    
                        coord_casa, coord_trabajo, coord_parque = datos[0], datos[1], datos[2]
                    
                        first_time = False 
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
         
                        else:
                            exit()
                    else:
                        while True:
                            # Se muestran los datos al usuario
                            print(f'coordenada [latitud, longitud] 1 : {coord_casa}')
                            print(f'coordenada [latitud, longitud] 2 : {coord_trabajo}')
                            print(f'coordenada [latitud, longitud] 3 : {coord_parque}')
                            print(f'La coordenada {coord} es la que está más al oriente')
                            print(f'La coordenada {compare_list} es la promedio de todos los puntos')
                            try:
                                opc_3 = int(input('Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú'))
                            except:
                                print('Error actualización')
                                exit()
                            if opc_3 == 1:
                                coord_new = []
                            
                                latitud = input('Latitud: ')
                                latitud = verif(latitud)
                                longitud = input('Longitud: ')
                                longitud = verif(longitud)
                                
                                coord_new.append(latitud)
                                coord_new.append(longitud)
                                datos[0] = coord_new
                                result = verif(datos)
                                if result == 1:
                                    break
                                else:
                                    print('Error coordenada')
                                    exit()
                                
                            elif opc_3 == 2:
                                coord_new = []
                                latitud = input('Latitud: ')
                                latitud = verif(latitud)
                                longitud = input('Longitud: ')
                                longitud = verif(longitud)
                                coord_new.append(latitud)
                                coord_new.append(longitud)
                                datos[1] = coord_new
                                result = verif(datos)
                                if result == 1:
                                    break
                                else:
                                    print('Error coordenada')
                                    exit()
                                    
                            elif opc_3 == 3:
                                coord_new = []
                                latitud = input('Latitud: ')
                                latitud = verif(latitud)
                                longitud = input('Longitud: ')
                                longitud = verif(longitud)
                                coord_new.append(latitud)
                                coord_new.append(longitud)
                                datos[2] = coord_new
                                result = verif(datos)
                                if result == 1:
                                    break
                                else:
                                    print('Error coordenada')
                                    exit()
                            elif opc_3 == 0:
                                break
                            else:
                                print('Error actualización')
                                exit()
                                
                # Opcion No 3
                if opc == 3:
                    matrix = [[6.211, -72.482, 2], 
                            [6.212, -72.470, 25], 
                            [6.105, -72.342, 25], 
                            [6.210, -72.442, 50]]
                    if datos == []:
                        print('Error sin registro de coordenadas') 
                        exit()
                    else:
                        info = datos
                        print(f'coordenada [latitud, longitud] 1 : {info[0]}')
                        print(f'coordenada [latitud, longitud] 2 : {info[1]}')
                        print(f'coordenada [latitud, longitud] 3 : {info[2]}')
                        try:
                            opcion = int(input(('Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión')))
                        except:
                            print('Error ubicación ')
                            exit()
                        if opcion == 1:
                            get_distance(info[0], matrix)
                        elif opcion == 2:
                            get_distance(info[1], matrix)
                        elif opcion == 3:
                            get_distance(info[2], matrix)
                        else:
                            print('Error ubicación')
                            exit() 
                        salir = 1   
                        while salir != 0:
                            salir = int(input('Presione 0 para salir'))
                            if salir == 0:
                                continue ### necesito que regrese al menu original
                # Opcion No 6
                elif opc == 6:
                    opc_fav = int(input('Seleccione opción favorita '))
                    if opc_fav in range(1, 6):
                        save_favort = menu[opc_fav-1]
                        menu.pop(opc_fav-1)
                        menu_full = [save_favort] + menu
                        primer_guess = int(input('Me separaron de mi hermano siamés, antes era un ocho y ahora soy un… la respuesta es:'))
                        if primer_guess == 3:
                            seg_guess = int(input('Parece un reloj de arena o el eslabón de una cadena: '))
                            if seg_guess == 8:
                                lista_ord = []
                                for i in menu_full:
                                    x = menu_full.index(i) + 1  
                                    menu_ok = f'{x}{i[1:]}'
                                    lista_ord.append(menu_ok)
                                    menu_fix = lista_ord
                                print(*menu_fix)
                                opc_2 =  int(input('Elija una opción '))
                                time.sleep(2)
                                os.system('cls')
                                print(f'Usted ha elegido la opción {opc_2}')
                    else:
                        print('Error')
                    break
                # Opcion No 7
                elif opc == 7:
                    print('Hasta pronto')
                    break
                # Opcion Dif de 1-7
                elif opc not in range(1, 8):
                    contador += 1
                    if contador == 3:
                        print('Error')
                        break
        else:
            print('Error') # Si la suma no es correcta sale ERROR
    else:
        print('Error') # Si la contraseña fue incorrecta sale ERROR
else:
    print('Error') # Si el usuario fue incorrecto sale ERROR
time.sleep(3)
os.system('cls')
