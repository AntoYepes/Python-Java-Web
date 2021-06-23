#%%
import os     

# funcion para actualizar la coord deseada
def refresh(lista):
    datos = []
    for i in lista:
        for k in  ["latitud","longitud"]:
            x = float(input(f'Ingrese la {k} de {i}'))
            datos.append(x)
        return datos

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
            
first_time = True  
while True:    
    opc = int(input('''
    1. Cambiar contraseña
    2. Ingresar coordenadas actuales
    : '''))
    if opc == 1:
        contraseña = int(input('Ingrese la contraseña actual: ')) # Se verifica la contraseña
        if contraseña == 83615:
            new_contraseña = int(input('Ingresa la nueva contraseña: '))        
        else:
            print('Error')
            break
    elif opc == 2:
        datos = []
        for i in ["casa","trabajo","parque"]:
            entrada = []
            for k in  ["latitud","longitud"]:
                x = float(input(f'Ingrese la {k} de {i}'))
                entrada.append(x)
            globals()[i] = entrada
            datos.append(globals()[i])
        
        first_time = False  
        coord_casa = datos[0]
        coord_trabajo = datos[1]
        coord_parque = datos[2]	
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

#%%
'''elif variable.strip() == 'Ubicar zona wifi más cercana'and indice == str(opc):
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
                                opcion = int(input(('Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión')))
                                if opcion == 1:
                                    cal_distance(info[0], matrix)
                                elif opcion == 2:
                                    cal_distance(info[1], matrix)
                                elif opcion == 3:
                                    cal_distance(info[2], matrix)
                                else:
                                    print('Error ubicación')
                                    exit() 
                                salir = 1   
                                while salir != 0:
                                    salir = int(input('Presione 0 para salir'))
                                    if salir == 0:
                                        break
                                    else:
                                        continue
                                break '''
# %%
