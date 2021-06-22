# %%
import os
import time
# funcion para actualizar la coord deseada
def refresh(lista):
    datos = []
    for i in lista:
        for k in  ["latitud","longitud"]:
            x = float(input(f'Ingrese la {k} de {i}'))
            datos.append(x)
        return datos

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
os.system('cls')

password = 83615
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
            first_time = True
            while True:
                # A continuacion se crea la lista que nos piden, utilizo ('\n') para que salte de linea 
                menu = ['1 Cambiar contraseña\n', '2 Ingresar coordenadas actuales\n', '3 Ubicar zona wifi más cercana\n', '4 Guardar archivo con ubicación cercana\n', '5 Actualizar registros de zonas wifi desde archivo\n','6 Elegir opción de menú favorita\n', '7 Cerrar sesión']
                print(*menu) # Imprimo la lista 
                opc = int(input('Elija una opción ')) # Creo una variable para darle la opcion al usuario de que elija el que desee, utilizo int porque necesito que sea un entero
                # Solo hago la opcion 6 con condicional porque el usuario eligira su opcion favorita
                if opc == 1:
                    contraseña = int(input('Ingrese la contraseña actual: ')) # Se verifica la contraseña
                    if contraseña == password:
                        new_contraseña = int(input('Ingresa la nueva contraseña: '))
                        password = new_contraseña 
                        continue       
                    else:
                        print('Error')
                        exit()
                elif opc == 2:
                    datos = []
                    for i in ["casa","trabajo","parque"]:
                        entrada = []
                        for k in  ["latitud","longitud"]:
                            x = float(input(f'Ingrese la {k} de {i}'))
                            entrada.append(x)
                        globals()[i] = entrada
                        datos.append(globals()[i])
                    
                    coord_casa = datos[0]
                    coord_trabajo = datos[1]
                    coord_parque = datos[2]	
                    print(type(coord_casa))
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
                                print(f'coordenada [latitud, longitud] 1 : {coord_trabajo}')
                                print(f'coordenada [latitud, longitud] 2 : {coord_casa}')
                                print(f'coordenada [latitud, longitud] 3 : {coord_parque}')
                                print(f'La coordenada {coord} es la que está más al oriente')
                                print(f'La coordenada {compare_list} es la promedio de todos los puntos')
                                
                                opc_3 = int(input('Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú'))
                                if opc_3 == 1:
                                    coordn = ['casa']
                                    coord_new = refresh(coordn)
                                    datos[0] = coord_new
                                    result = verif(datos)
                                    if result == 1:
                                        break
                                    else:
                                        print('Error coordenada')
                                        exit()
                                    
                                elif opc_3 == 2:
                                    coordn = ['trabajo']
                                    coord_new = refresh(coordn)
                                    datos[1] = coord_new
                                    result = verif(datos)
                                    if result == 1:
                                        break
                                    else:
                                        print('Error coordenada')
                                        exit()
                                elif opc_3 == 3:
                                    coordn = ['parque']
                                    coord_new = refresh(coordn)
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
                elif opc == 6: 
                    contador = 0
                    while True:
                        lista = None
                        if lista == None:
                            pass
                        else:
                            print(*lista)
                        opc_fav = int(input('Seleccione opción favorita ')) # Creo otra variable para pedirle al usuario que ingrese la opcion favorita, uso int para convertirlo en entero
                        if opc_fav in range(1, 6): # Uso un condicional con range, ya que los favoritos deben ser entre 1 y 5
                            del_favort = menu.pop((opc_fav-1)) # Como menu es una lista, utilizo pop para que me elemine el item que le diga, pongo (opc_fav-1) porque recuerda que los indices inician 0,1,2,3,... si la opcion favorita es la 3, su posicion correcta seria 2 en indices, es por eso que le resto 1.
                            menu_full = [del_favort] + menu # Aca vuelvo a introducir la opcion favorita pero de primeras. ([del_favort] + menu): acá al tener dos listas, si las sumo, del_favort se ubica de primera.
                            # A continuacion creo una variable, para la primera adivinanza, con input para que el usurio ingrese el numero
                            primer_guess = int(input('Me separaron de mi hermano siamés, antes era un ocho y ahora soy un… la respuesta es:'))
                            if primer_guess == 3: # Uso condicional para verificar el numero ingresado por el usuario
                                seg_guess = int(input('Parece un reloj de arena o el eslabón de una cadena: ')) # Si el numero anterior resulto correcto, ahora si se le pide el segundo numero
                                if seg_guess == 8: # Se verifica el segundo num
                                    lista = []
                                    for i in menu_full: # Creo un ciclo for porque necesito recorrer cada item de la lista ya completa, con la opc favorita de primeras
                                        x = menu_full.index(i) + 1  # Creo una variable, utilizo la lista completa con index  para que ubique cada item y le sumo 1; porque recuerda que 0,1,2,3... y mi opc favorita esta en el index 0, pero el numero que quiero utilizar es 1, es por eso que le sumo 1.
                                        menu_fix = f'{x}{i[1:]}' # Utilizo format co las variable anterior. la x pondra 1,2,3,4 ( porque tomo los indices y les sumo 1 a todos), la i[1:] toma cada opcion de la lista, sin tener en cuenta los numero
                                        lista.append(menu_fix)
                                        print(menu_fix)
                                    
                                    opc_2 =  int(input('Elija una opción ')) # Se crea otra variable para que la persona eleija la opc que desee
                                    time.sleep(2)
                                    os.system('cls')
                                    print(f'Usted ha elegido la opción {opc_2}')
                                    for s in lista:
                                        indice = s[0]
                                        if 'Cambiar contraseña' in s and indice == str(opc_2):
                                            contraseña = int(input('Ingrese la contraseña actual: ')) # Se verifica la contraseña
                                            if contraseña == password:
                                                new_contraseña = int(input('Ingresa la nueva contraseña: ')) 
                                                password = new_contraseña
                                                break
                                            else:
                                                print('Error')
                                                exit()
                                    
                                        if 'Ingresar coordenadas actuales' in s and indice == str(opc_2):
                                            datos = []
                                            for i in ["casa","trabajo","parque"]:
                                                entrada = []
                                                for k in  ["latitud","longitud"]:
                                                    x = float(input(f'Ingrese la {k} de {i}'))
                                                    entrada.append(x)
                                                globals()[i] = entrada
                                                datos.append(globals()[i])
                                            
                                            coord_casa = datos[0]
                                            coord_trabajo = datos[1]
                                            coord_parque = datos[2]	
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
                                                        print(f'coordenada [latitud, longitud] 1 : {coord_trabajo}')
                                                        print(f'coordenada [latitud, longitud] 2 : {coord_casa}')
                                                        print(f'coordenada [latitud, longitud] 3 : {coord_parque}')
                                                        print(f'La coordenada {coord} es la que está más al oriente')
                                                        print(f'La coordenada {compare_list} es la promedio de todos los puntos')
                                                        
                                                        opc_3 = int(input('Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú'))
                                                        if opc_3 == 1:
                                                            coordn = ['casa']
                                                            coord_new = refresh(coordn)
                                                            datos[0] = coord_new
                                                            result = verif(datos)
                                                            if result == 1:
                                                                break
                                                            else:
                                                                print('Error coordenada')
                                                                exit()
                                                            
                                                        elif opc_3 == 2:
                                                            coordn = ['trabajo']
                                                            coord_new = refresh(coordn)
                                                            datos[1] = coord_new
                                                            result = verif(datos)
                                                            if result == 1:
                                                                break
                                                            else:
                                                                print('Error coordenada')
                                                                exit()
                                                        elif opc_3 == 3:
                                                            coordn = ['parque']
                                                            coord_new = refresh(coordn)
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
                                    # Condicional para la opcion 7 que es salir, como desero salir despues de imprimir lo que deseo pongo break, para terminar el ciclo while
                                    if opc_2 == 7:
                                        print('Hasta pronto')
                                        exit()
                                    # Condicional para los ingresos diferentes de 1-7
                                    elif opc_2 not in range(1, 8): # Por eso aca utilizo not in, porque tendre en cuenta los numeros que no estan en el rango de 1-7
                                        contador += 1 # Si la persona ingresa otro numero dif de 1-7 el contador comienza a sumar de a uno
                                        if contador == 3: # Cuando el contador ya es 3, imprime error y termina el ciclo while con break
                                            print('Error')
                                            exit()  
                                            
                                else:
                                    print('Error')
                                    break   
                            else:
                                print('Error')
                                break
                        # else de 1-5                      
                        else:
                            print('Error')
                            exit()
                # Condicional para la opcion 7 que es salir, como desero salir despues de imprimir lo que deseo pongo break, para terminar el ciclo while
                elif opc == 7:
                    print('Hasta pronto')
                    exit()
                # Condicional para los ingresos diferentes de 1-7
                elif opc not in range(1, 8): # Por eso aca utilizo not in, porque tendre en cuenta los numeros que no estan en el rango de 1-7
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
os.system('cls')