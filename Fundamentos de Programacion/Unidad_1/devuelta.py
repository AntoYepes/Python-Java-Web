precio = int(input('Ingrese el precio del producto: '))
pago = int(input('Ingrese la cantidad de pago: '))

cambio = pago - precio
faltante = precio - pago

if cambio < 0:
    print(f'Falta dinero en el pago, el dinero faltante es: {faltante}')
elif cambio == 0:
    print('Se ha pagado completo, no se necesita dar cambio')
if cambio > 0:
    print(f'El cambio a dar es: {cambio}')