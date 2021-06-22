import math
while True:
    menu_cal = int(input('''
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Logaritmo
    5. Coseno
    6. Seno
    7. Raiz cuadrada
    8. Decimal a binario
    9. Binari a decimal
    0. Salir
    :'''))
    if menu_cal == 1:
        try:
            num_1 = int(input('Ingresa un numero: '))
            num_2 = int(input('Ingresa un numero: '))
            print(num_1 + num_2)
        except :
            print('Error')
    elif menu_cal == 2:
        try: 
            num_1 = int(input('Ingresa un numero: '))
            num_2 = int(input('Ingresa un numero: '))
            print(num_1 - num_2)
        except:
            print('Error')
    elif menu_cal == 3:
        try:
            num_1 = int(input('Ingresa un numero: '))
            num_2 = int(input('Ingresa un numero: '))
            print(num_1 * num_2)
        except:
            print('Error')
    elif menu_cal == 4:
        try:
            num_1 = int(input('Ingresa un numero: '))
            print(math.log(num_1))
        except:
            print('Error')
    elif menu_cal == 5:
        try:
            num_1 = int(input('Ingresa un numero: '))
            print(math.cos(num_1))
        except:
            print('Error')
    elif menu_cal == 6:
        try:
            num_1 = int(input('Ingresa un numero: '))
            print(math.sin(num_1))
        except:
            print('Error')
    elif menu_cal == 7:
        try:
            num_1 = int(input('Ingresa un numero: '))
            print(math.sqrt(num_1))
        except:
            print('Error')
    elif menu_cal == 8:
        try:
            num_1 = int(input('Ingresa un numero: '))
            print(bin(num_1))
        except:
            print('Error')
    elif menu_cal == 9:
        try:
            num_1 = bin(input('Ingresa un numero: '))
            print(int(num_1, 2))
        except:
            print('Error')
    elif menu_cal == 0:
        break
    else:
        print('Ingrese valor numerico: ')
