from datetime import datetime 

while True:
    opc = int(input('''
    1. Saludar
    2. Es par
    3. Promedio
    4. Modulo
    5. Porcentaje
    6. Potencia
    0. Salir
    '''))
    if opc == 1:
        todays_date = datetime.now()
        hora = todays_date.hour
        if 00 < hora < 12:
            print('Buenos dias!')
        elif 12 <= hora < 18:
            print('Buenas tardes!')
        elif 18 <= hora < 24:
            print('Buenas noches!')
        
    elif opc == 2:
        numero = int(input('Ingresa el numero para verificar: '))
        if numero % 2 == 0:
            print(f'El número {numero} es par.')
        else:
            print(f'El número {numero} es impar.')
    elif opc == 3:
        x, y, z, w, t = map(float, input("Ingrese 5 notas separados por espacio: ").split())
        promedio = (x + y + z + w + t)/2
        print(promedio)
    elif opc == 4:
        num1 = int(input('Ingrese el primer numero: '))
        num2 =   int(input('Ingrese el segundo numero: '))
        print(num1 % num2)
    elif opc == 5:
        num3 =  int(input('Ingresa el numero: '))
        result = num3 / 100
        print(f'{result} %')
    elif opc == 6:
        num_base = int(input('Ingrese el numero base: '))
        num_exp =  int(input('Ingrese el numero de potencia: '))
        print(num_base ** num_exp)
    elif opc == 0:
        break
    else:
        print('Opcion incorrecta, verifica el num ingresado ')