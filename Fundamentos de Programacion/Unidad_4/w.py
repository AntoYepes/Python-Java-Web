while True:
    menu = ['1 Cambiar contraseña\n', '2 Ingresar coordenadas actuales\n', '3 Ubicar zona wifi más cercana\n', '4 Guardar archivo con ubicación cercana\n', '5 Actualizar registros de zonas wifi desde archivo\n','6 Elegir opción de menú favorita\n', '7 Cerrar sesión']
    print(*menu)
    salir = 1   
    while salir != 0:
        salir = int(input('Presione 0 para salir'))
        if salir == 0:
            continue ### necesito que regrese al menu original
        
    