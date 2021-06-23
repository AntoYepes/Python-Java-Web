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

datos = []
password = 83615
# Mensaje de bienvenida
print('Bienvenido al sistema de ubicación para zonas públicas WIFI')
time.sleep(1) 
os.system('clear')
# Pedimos por consola el usuario
usuario = input('Ingrese el usuario: ')
if int(usuario) == 51638: # Se verifica el usuario
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
                                os.system('clear')
                                print(f'Usted ha elegido la opción {opc_2}')
                    else:
                        print('Error')
                    break
                elif opc == 7:
                    print('Hasta pronto')
                    break
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
os.system('clear')
