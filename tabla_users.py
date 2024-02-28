import json

import pandas as pd

#abrimos y cargamos el json que hemos creado en el ejercicio anterior
f = open('users.json')
usuariosHasheados = json.load(f)

#para trabajar  con pandas, hay que crear  un dataframe df , entonces lo creamos con la variable que hemos cargado el json y lo convertimos a excel
df = pd.json_normalize(usuariosHasheados)
df.to_excel('usuarios.xlsx')






