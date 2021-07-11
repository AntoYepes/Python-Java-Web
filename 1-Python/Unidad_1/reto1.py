#%% RETO 1
# Importo las librerias que necesito mas adelante en el codigo
import os # Esta libreria sirve para la consola
import time # Esta libreria importo el tiempo
# Imprimo el mensaje de bienvenida
print('Bienvenido al sistema de ubicación para zonas públicas WIFI') 
time.sleep(1)  # Usando la libreia le digo al sistema que me muestre la info anterior 1seg
os.system('cls') # Usando esta libreria le digo a la consola que limpie, uso cls es por ser windows
# A continuacion uso try y except para verificar que lo que me ingresen sea un numero, con el except si me ingresan otro caracter saldra el mensaje: Ingresa un numero
try:
    # Pedimos por consola el usuario
    usuario = input('Ingrese el usuario: ')
    if int(usuario) == 51638: # Se verifica el usuario con el condicional, recuerda que estoy comparando los digitos deben ser iguales, es decir: int con int, str con str...
        contraseña = int(input('Ingrese la contraseña: ')) # Pedimos la contraseña
        if contraseña == 83615: # Se verifica la contraseña
            num_1 = 638 # Creo una variable para registrar el 1er numero
            num_2 = (3*5-9-3 or  10 % 3 + 2) or ((10 // 2) - 2) # Creo la 2nd variable con diferentes operaciones como lo piden. Mira que uso or para indicar que son varias, cualquiera debe de dar el mismo resultado es decir 3.
            captcha = input(f'Resuelva la suma {num_1} + {num_2} = ') # Creo la variable Captcha, la suma para comprobar si el inicio de sesion corresponde a un usuario. Aca uso f que significa format, lo que hace es copiar texto tomando las variables num_1 y num_2
            if int(captcha) == 641: # Acá se verifica que la suma que se solicita si este correcta, usamos un condicional
                print('Sesión iniciada') # Si la suma es correcta sale sesion iniciada
            else:
                print('Error') # Si la suma no es correcta sale ERROR
        else:
            print('Error') # Si la contraseña fue incorrecta sale ERROR
    else:
        print('Error') # Si el usuario fue incorrecto sale ERROR
    time.sleep(1)
    os.system('cls')
except:
    print('Ingresa un numero: ')


# %%
