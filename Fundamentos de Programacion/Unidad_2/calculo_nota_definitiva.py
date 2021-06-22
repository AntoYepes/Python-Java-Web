import numpy as np
diccionario = {'1025':{'notas':[3.5,4.5,5.0,3.5],'porcentajes':[20,20,30,30]},'1026':{'notas':[4.0,3.2,5.0,4.2],'porcentajes':[25,20,30,25]}}
    
for i in diccionario:
    grade = diccionario[i]['notas']
    porcent = diccionario[i]['porcentajes']
    my_list = list(map(lambda x: x / 100, porcent))
    print(sum(np.multiply(grade, my_list)))

