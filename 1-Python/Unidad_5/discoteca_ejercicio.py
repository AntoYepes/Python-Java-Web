def entrada_disco(edad):
    if edad >= 18:
        return 'Bienvenido'
    else:
        return 'Lo siento no puede ingresar'
    
result = entrada_disco(17)
print(result)