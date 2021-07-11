#%% AHORCADITO
import random 
palabras = {1:'Cartagena', 2:'Cucuta', 3:'Medellin', 4:'Bogota', 5:'Cali', 6:'Armenia'}

def choose_word(diccionario, start=1, end=7):
    palabra = 'Pasto'
    rand = random.randint(start, end)
    if rand in list(diccionario.keys()):
        palabra = diccionario[rand]
    return palabra

def enmascarar2(palabra, caracter='-'):
    espacio = caracter * len(palabra)
    return espacio

def reemplazarCaracter(palabra, palab_modif, caracter):
    aux = list(palab_modif)
    count = palabra.lower().count(caracter)
    cont = 0
    if count > 0:
        for i in palabra:
            if i.lower() == caracter.lower():
                aux[cont] = caracter.lower()
            cont+=1
        return "".join(aux)
    else:
        return palab_modif
    
vida = 7
error = 0
word = choose_word(palabras)   
word_enmasc = enmascarar2(word)
print('Adivina alguna de las ciudades de Colombia!')
print(f'Palabra de {len(word)} letras')
print(word_enmasc)
while True:
    letra_user = input('Ingrese una letra')
    if letra_user in word.lower():
        word_enmasc = reemplazarCaracter(word, word_enmasc, letra_user)
        print(word_enmasc)
    else:
        vida = vida - 1
        print(f'fallaste, te quedan {vida} intentos')
    if vida == 0:
        print('lo siento, vuelve pronto...')
        print(f'la palabra era {word}')
        break
    if word_enmasc == word:
        print('En hora buena, GANASTE!!!')
        break
# %%
