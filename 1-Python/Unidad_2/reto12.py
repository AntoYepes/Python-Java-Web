# %%
import os
import time
import math
# Mensaje de bienvenida
print('Bienvenido al sistema de ubicación para zonas públicas WIFI')
time.sleep(1) 
os.system('cls')
# Pedimos por consola el usuario
usuario = input('Ingrese el usuario: ')
if int(usuario) == 51638: # Se verifica el usuario
    contraseña = int(input('Ingrese la contraseña: ')) # Se verifica la contraseña
    if contraseña == 83615: # Se verifica la contraseña
        num_1 = 638 # Primer No
        num_2 = (3*5-9-3 or  10 % 3 + 2) or ((10 // 2) - 2) # Segundo No
        captcha = input(f'Resuelva la suma {num_1} + {num_2} = ') # Captcha, la suma para comprobar si el inicio de sesion corresponde a un usuario
        if int(captcha) == 641:
            print('Sesión iniciada') # Si la suma es correcta sale sesion iniciada
            menu = ['1 Cambiar contraseña\n', '2 Ingresar coordenadas actuales\n', '3 Ubicar zona wifi más cercana\n', '4 Guardar archivo con ubicación cercana\n', '5 Actualizar registros de zonas wifi desde archivo\n','6 Elegir opción de menú favorita\n', '7 Cerrar sesión']
            print(*menu)
            contador = 0
            while True:
                opc = int(input('Elija una opción '))
                if opc == 6:
                    opc_fav = int(input('Seleccione opción favorita '))
                    if opc_fav in range(1, 6):
                        del_favort = menu.pop((opc_fav-1))
                        menu_full = [del_favort] + menu
                        primer_guess = int(input('Me separaron de mi hermano siamés, antes era un ocho y ahora soy un… la respuesta es:'))
                        if primer_guess == 3:
                            seg_guess = int(input('Parece un reloj de arena o el eslabón de una cadena: '))
                            if seg_guess == 8:
                                for i in menu_full:
                                    x = menu_full.index(i) + 1  
                                    menu_fix = print(f'{x}{i[1:]}')
                                opc_2 =  int(input('Elija una opción '))
                                time.sleep(2)
                                os.system('cls')
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
os.system('cls')
