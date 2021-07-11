#%%
from datetime import datetime 

todays_date = datetime.now()
hora = todays_date.hour
if 00 < hora < 12:
    print('Buenos dias!')
elif 18 <= hora < 24:
    print('Buenas noches!')
elif 12 <= hora < 18:
    print('Buenas tardes!')

# %%
