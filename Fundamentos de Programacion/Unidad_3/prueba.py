with open('prueba.txt', 'r+') as f:
    cont = f.readlines()
    for i in cont:
        p = i.split(',')
        precio = int(p[3])
        iva = int(p[4])
        cant = int(p[2])
        print('Codigo: ' , p[0],  '\n', 'Nombre: '  , p[1], '\n', 'Cantidad: ' , p[2], '\n','Precio', p[3], '\n', 'Iva:', p[4], '\n', 'Subtotal:', precio*cant, '\n', 'Subt + iva:', (precio*cant)*(1+(iva/100)), '\n', '-------------------')
        
# print(itemgetter(*indexes)(listas_clean))
#x = [i for i in listas_clean if i.isdigit()]
            #print(x)
            
#datos = []
#for j in indexes:
#    datos.append(listas_clean[j])
    
#    print(itemgetter(*indexes)(datos))