import os
ruta=os.getcwd()+'/users/lista.txt'
def pintar_opciones(lista_opciones):
    for ind,opcion in enumerate(lista_opciones):
        print(f'{ind+1}. {opcion}')
def autenticar(username,password):
    with open(ruta) as file_users:
       for user in file_users.readlines():
           lista_usuarios=user.split(';')
           if lista_usuarios[0] == username and lista_usuarios[1]==password and lista_usuarios[2]=='1':
               return True,lista_usuarios[5:],lista_usuarios[3]
    return False,[],''
flag,opciones,etiqueta=autenticar('user1', 'password1')
pintar_opciones(opciones)