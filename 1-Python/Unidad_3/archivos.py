# r+ Lectura y escritura
# w Solo lectura
# rb+ Lectur y escritura en modo binario
# w+ Escritura y lectura
# a Añadir
# a+ Añade y lectura
# seek(bite) -> 
with open('file.txt', 'w') as f:
    f.write('Hola')
    for i in f.readlines():
        print(i)
        
