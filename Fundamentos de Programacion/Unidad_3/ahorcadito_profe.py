# debemos tener un grupo de palabras 
# organizar las palabras en un diccionario
# Enmascarar la palabra
# indicar de que tamaño es la palabra que se va presentar al usuario
palabras = {4:'Cartagena',2:'Cucuta',3:'Medellin',1:'Bogota',5:'Bucaramanga',6:'Armenia',7:'Cali'}

def escoger_palabra(diccionario,inicio=1, fin=7):
    import random as rdm
    palabra = 'Ibague'
    rand = rdm.randint(inicio,fin)
    if rand in list(diccionario.keys()):
        palabra = diccionario[rand]
    return palabra


def enmascarar(palabra,caracter='-' ):
    espacio = caracter * len(palabra)
    return espacio

def reemplazarCaracter(palabra,palabra_modificada,caracter):
    aux = list(palabra_modificada)
    count = palabra.lower().count(caracter)
    cont = 0
    if count > 0:
        for letra in palabra:
            if letra.lower() == caracter.lower():
                aux[cont] = caracter.upper()
            cont += 1
        return "".join(aux)
    else:
        return palabra_modificada

vida = 7
error = 0
word = escoger_palabra(palabras)
wordmodify = enmascarar(word)
print('Adivina la palbra de ciudades colombianas ')
print(f'Palabra de {len(word)} letras ')
print(wordmodify)
while True:
    letra_user=input('Ingrese una letra ')
    if letra_user in word.lower():
        wordmodify = reemplazarCaracter(word,wordmodify,letra_user)
        print(wordmodify)
    else:
        vida = vida -1
        print(f'Fallaste te quedan {vida} intentos ')
        if vida == 0:
            print('Lo siento viejo, vuelve pronto...')
            print(f'La palabra a adivinar era: {word} ')
            break
    if wordmodify == word.upper():
        print('En hora buena ganaste ')
        break
print('Fin del programa.... ')
        




