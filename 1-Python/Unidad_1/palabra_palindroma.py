#%%
word = input('Ingrese la palabra a verificar: ')
if word == word[::-1]:
    print('Palindroma')
else:
    print('No es palindroma')
#%%
texto = input('Ingrese la palabra a verificar: ')
invertida = ''
original_invertida = ''
for i in range(len(texto)-1, -1, -1):
    letra = texto[i]
    if letra != '':
        invertida += letra
for j in range(0, len(texto)+1):
    letra = texto[j]
    if letra != '':
        original_invertida += letra
    
if invertida == original_invertida:
    print('Palindroma')
else:
    print('No palindroma')
#%%