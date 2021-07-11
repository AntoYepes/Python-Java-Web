#%%
def get_digit(number, n):
    return number // 10**n % 10

num = int(input('Ingrese el numero: '))
cant = len(str(num)) # int
if (get_digit(num, )**cant + get_digit(num, )**cant + get_digit(num, )**cant) == num:
    print('Es un número de Armstrong')
else:
    print('No es un numero Armstrong')

# %%
num = int(input('Ingrese el numero: '))
cant = len(str(num)) # int
sum_digit = 0
original = num
while num > 0:
    digit = num % 10
    sum_digit += digit ** cant
    num = num // 10

if num == original:
    return True
else:
    return False

print(sum_digit)

# %%
tx = int(input('x'))
x // 10**4 % 10
