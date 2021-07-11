datos = [[5.99, -72.499]]
wifi = [[6.211, -72.482, 2], 
        [6.212, -72.470, 25], 
        [6.210, -72.442, 50]]
recorrido = ['765', 'bicicleta', '124segundos']
informacion = {'actual' : datos[0],'zonawifi1' : wifi[0], 'recorrido' : recorrido}
print(informacion)
mensaje = int(input('¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal  '))
while True:
    if mensaje == 1:
        print('Exportando archivo')
        exit()
    elif mensaje == 0:
        break # volver al menu?
        