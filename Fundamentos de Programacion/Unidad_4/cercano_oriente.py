 # Calculo para el valor mas cercano al oriente
datos = [[6.212, -72.499], [6.105, -72.501], [6.210, -72.345]]
given_value = -72.321 
flattened = [val for sublist in datos for val in sublist]
absolute_difference_function = lambda list_value : abs(list_value - given_value)
closest_value = min(flattened, key=absolute_difference_function)
print(closest_value)
i=0
new_list=[]
while i<len(flattened):
    new_list.append(flattened[i:i+2])
    i+=2
indx = [ele for i, ele in new_list].index(closest_value)
coord = indx+1
print(new_list)
print(flattened)   
print(coord)