with open('prueba_2.txt', 'r+') as f:
    for i, l in enumerate(f.readlines()):
        p = l.split(',')
        product = p[1]
        if len(p) < 5:
            print(f'Faltan valores en la fila {i+1}')
            exit()
        else:
            try:
                cant = int(p[2])
                iva = float(p[4]) / 1000
                precio = int(p[3])
            except :
                print(f'Hay valores no numericos en la fila {i+1}')
                exit()
        subtotal = (cant*iva) * (1 + iva)
        print(f'Item: {product}, cantidad: {cant}, Subtotal: {subtotal}')
        
