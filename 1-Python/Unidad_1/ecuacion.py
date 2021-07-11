#%% ECUACION
# ecuac algebraica de 4 incognitas, codifica la expresion en partes simples

from sympy import symbols, Eq, solve

x, y, z = symbols('x,y,z')
# Ecuaciones
eq1 = Eq((x+y+z), 1)
print("Equation 1:")
print(eq1)
  
eq2 = Eq((x-y+2*z), 1)
print("Equation 2")
print(eq2)
  
eq3 = Eq((2*x-y+2*z), 1)
print("Equation 3")
  
# Resolucion
print("Values of 3 unknown variable are as follows:")
print(solve((eq1, eq2, eq3), (x, y, z)))
# %%
