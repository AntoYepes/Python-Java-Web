import os
import time
import math 

# Funcion para verificar los limites y la long de cada entrada
def verif(info):
    for i in info:
        if len(i) != 2:
            print('Error')
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
 
# Mensaje de bienvenida
print('Bienvenido al sistema de ubicación para zonas públicas WIFI')
time.sleep(1) 
os.system('clear')

datos = []
password = 83615
menu = ['1 Cambiar contraseña\n', '2 Ingresar coordenadas actuales\n', '3 Ubicar zona wifi más cercana\n', '4 Guardar archivo con ubicación cercana\n', '5 Actualizar registros de zonas wifi desde archivo\n','6 Elegir opción de menú favorita\n', '7 Cerrar sesión']
menu_fix = menu
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
            contador = 0 # Creo una variable contador porque mas adelante necesitare contar errores como lo solicitan. la inicio en 0
            # Creo el ciclo, porque es un menu
            while True: 
                print(*menu_fix) # Imprimo la lista
                opc = int(input('Elija una opción ')) # Creo una variable para darle la opcion al usuario de que elija el que desee, utilizo int porque necesito que sea un entero
                #if opc in range(1, 7):
                #    print(f'Usted ha elegido la opción {opc}')
                # Solo hago la opcion 6 con condicional porque el usuario eligira su opcion favorita
                if opc == 6:
                    while True:
                        opc_fav = int(input('Seleccione opción favorita ')) # Creo otra variable para pedirle al usuario que ingrese la opcion favorita, uso int para convertirlo en entero
                        primer_guess = int(input('Me separaron de mi hermano siamés, antes era un ocho y ahora soy un… la respuesta es:'))
                        if primer_guess == 3: # Uso condicional para verificar el numero ingresado por el usuario
                            seg_guess = int(input('Parece un reloj de arena o el eslabón de una cadena: ')) # Si el numero anterior resulto correcto, ahora si se le pide el segundo numero
                            if seg_guess == 8: # Se verifica el segundo num
                                if opc_fav in range(1, 6): # Uso un condicional con range, ya que los favoritos deben ser entre 1 y 5
                                    save_favort = menu_fix[opc_fav - 1]
                                    menu_fix.pop((opc_fav - 1)) # Como menu es una lista, utilizo pop para que me elemine el item que le diga, pongo (opc_fav-1) porque recuerda que los indices inician 0,1,2,3,... si la opcion favorita es la 3, su posicion correcta seria 2 en indices, es por eso que le resto 1.
                                    menu_full = [save_favort] + menu_fix # Aca vuelvo a introducir la opcion favorita pero de primeras. ([del_favort] + menu): acá al tener dos listas, si las sumo, del_favort se ubica de primera.
                                    #menu_fix = menu_full
                                    # A continuacion creo una variable, para la primera adivinanza, con input para que el usurio ingrese el numero
                                lista = []
                                lista2 = []
                                for i in menu_full: # Creo un ciclo for porque necesito recorrer cada item de la lista ya completa, con la opc favorita de primeras
                                    x = menu_full.index(i) + 1  # Creo una variable, utilizo la lista completa con index  para que ubique cada item y le sumo 1; porque recuerda que 0,1,2,3... y mi opc favorita esta en el index 0, pero el numero que quiero utilizar es 1, es por eso que le sumo 1.
                                    menu2 = f'{x}{i[1:]}' # Utilizo format co las variable anterior. la x pondra 1,2,3,4 ( porque tomo los indices y les sumo 1 a todos), la i[1:] toma cada opcion de la lista, sin tener en cuenta los numeros.
                                    text = i[1:].strip() 
                                    lista.append(text)
                                    lista2.append(menu2)
                                    menu_fix = lista2                            
                                #opc_2 =  int(input('Elija una opción ')) # Se crea otra variable para que la persona eleija la opc que desee
                                time.sleep(2)
                                os.system('clear')
                                break
                            else:
                                print('Error')
                                break
                        else:
                            print('Error')
                            break
                # Opcion del 1-7
                elif opc in range(1, 8):
                    for n in menu_fix:
                        variable = f'{n[1:]}'
                        indice = n[0]
                        #print(opc)
                        #print(indice)
                        #print(variable.strip())
                        # Opcion No1
                        if variable.strip() == 'Cambiar contraseña' and indice == str(opc):
                            contraseña = int(input('Ingrese la contraseña actual: ')) # Se verifica la contraseña
                            if contraseña == password:
                                new_contraseña = int(input('Ingresa la nueva contraseña: '))
                                password = new_contraseña 
                                break       
                            else:
                                print('Error')
                                exit()
                        # Opcion No2
                        elif variable.strip() == 'Ingresar coordenadas actuales' and indice == str(opc):
                            datos = []
                            #for i in ["casa","trabajo","parque"]:
                            #    entrada = []
                            #    for k in  ["latitud","longitud"]:
                            #        x = float(input(f'Ingrese la {k} de {i}'))
                            #        entrada.append(x)
                            #    globals()[i] = entrada
                            #    datos.append(globals()[i])
                            lat_casa = float(input('Latitud casa: '))
                            lon_casa = float(input('Longitud casa: '))
                            lat_trab = float(input('Latitud trabajo: '))
                            lon_trab = float(input('Longitud trabajo: '))
                            lat_parque = float(input('Latitud parque: '))
                            lon_parque = float(input('Longitud parque: '))
                     
                            coord_casa, coord_trabajo, coord_parque = [], [], []
                            coord_casa.append(lat_casa)
                            coord_casa.append(lon_casa)
                            coord_trabajo.append(lat_trab)
                            coord_trabajo.append(lon_trab)
                            coord_parque.append(lat_parque)	
                            coord_parque.append(lon_parque)	
                            datos.append(coord_casa)
                            datos.append(coord_trabajo)
                            datos.append(coord_parque)
                            
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
                                        
                                if first_time == False:
                                    while True:
                                        # Se muestran los datos al usuario
                                        print(f'coordenada [latitud, longitud] 1 : {coord_casa}')
                                        print(f'coordenada [latitud, longitud] 2 : {coord_trabajo}')
                                        print(f'coordenada [latitud, longitud] 3 : {coord_parque}')
                                        print(f'La coordenada {coord} es la que está más al oriente')
                                        print(f'La coordenada {compare_list} es la promedio de todos los puntos')
                                        
                                        opc_3 = int(input('Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú'))
                                        if opc_3 == 1:
                                            coord_new = []
                                            coord_latcasa = float(input('Latitud casa: '))
                                            coord_loncasa = float(input('Longitud casa: '))
                                            coord_new.append(coord_latcasa)
                                            coord_new.append(coord_loncasa)
                                            datos[0] = coord_new
                                            result = verif(datos)
                                            if result == 1:
                                                break
                                            else:
                                                print('Error coordenada')
                                                exit()
                                            
                                        elif opc_3 == 2:
                                            coord_new = []
                                            coord_lattrab = float(input('Latitud trabajo: '))
                                            coord_lontrab = float(input('Longitud trabajo: '))
                                            coord_new.append(coord_lattrab)
                                            coord_new.append(coord_lontrab)
                                            datos[1] = coord_new
                                            result = verif(datos)
                                            if result == 1:
                                                break
                                            else:
                                                print('Error coordenada')
                                                exit()
                                        elif opc_3 == 3:
                                            coord_new = []
                                            coord_latparq = float(input('Latitud parque: '))
                                            coord_lonparq = float(input('Longitud parque: '))
                                            coord_new.append(coord_latparq)
                                            coord_new.append(coord_lonparq)
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
                            else:
                                exit()
                        # Opcion No7                                            
                        elif variable.strip() == 'Cerrar sesión' and indice == str(opc):
                            print('Hasta pronto')
                            exit()  
                else:
                    contador += 1 # Si la persona ingresa otro numero dif de 1-7 el contador comienza a sumar de a uno
                    if contador == 3: # Cuando el contador ya es 3, imprime error y termina el ciclo while con break
                        print('Error')
                        exit()
        else:
            print('Error') # Si la suma no es correcta sale ERROR
    else:
        print('Error') # Si la contraseña fue incorrecta sale ERROR
        exit()
else:
    print('Error') # Si el usuario fue incorrecto sale ERROR
    exit()
time.sleep(3)
os.system('clear')