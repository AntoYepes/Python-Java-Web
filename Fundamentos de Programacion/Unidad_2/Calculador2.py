#%% Menu con while
import os
import time
 
# Se imprime la calculadora con ascii art
print('''
   _____________________
  /                 `   \\
  |  .-----------.  |   |-----.
  |  |           |  |   |-=---|
  |  | Calcula-  |  |   |-----|
  |  |    dora   |  |   |-----|
  |  |           |  |   |-----|
  |  `-----------'  |   |-----'/\\
   \________________/___'     /  \\
      /                      / / /
     / //               //  / / /
    /                      / / /
   / _/_/_/_/_/_/_/_/_/_/ /   /
  / _/_/_/_/_/_/_/_/_/_/ /   /
 / _/_/_/_______/_/_/_/ / __/
/______________________/ /    
\______________________\/
''')
# Se crea el menu con while true
while True:
    print('''
  _    _ ______ _      _      ____  
 | |  | |  ____| |    | |    / __ \ 
 | |__| | |__  | |    | |   | |  | |
 |  __  |  __| | |    | |   | |  | |
 | |  | | |____| |____| |___| |__| |
 |_|  |_|______|______|______\____/                            
          ''')
    # Se piden los numeros de primeras
    num_1 = int(input('Ingresa el primer numero: '))
    num_2 = int(input('Ingresa el segundo numero: '))
    try:
        opc = int(input('''
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Salir
        :'''))
        if opc == 1:
            print(num_1 + num_2)
        elif opc == 2:
            print(num_1 - num_2)
        elif opc == 3:
            print(num_1 * num_2)
        elif opc == 4:
            print(num_1 / num_2)
        elif opc == 5:
            print("""
        _                
        | |               
        | |__  _   _  ___ 
        | '_ \| | | |/ _ \\
        | |_) | |_| |  __/
        |_.__/ \__, |\___|
                __/ |     
               |___/      
                    """)
            break
        else:
            print('Opcion incorrecta, vuelve a intentarlo!')
        # Se limpia consola
        time.sleep(1)
        os.system('cls')
    except:
        print('Ingrese solo un numero: ')
# %%
