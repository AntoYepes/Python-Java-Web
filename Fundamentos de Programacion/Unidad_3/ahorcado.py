#%%
import ast
with open('ahorcado.txt', 'r+') as f:
    contents = f.read()
    dictionary = ast.literal_eval(contents) # To read a dictionary from a file
    print(dictionary)
    
# %%
import ast
import numpy as np
with open('ahorcado.txt', 'r+') as f:
    contents = f.read()
    dictionary = ast.literal_eval(contents) # To read a dictionary from a file
    dataMatrix = np.array([dictionary[i] for i in dictionary.keys()])
