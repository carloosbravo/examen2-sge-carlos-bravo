import hashlib
import pandas as pd
import json


#leemos el json de los users y lo cargamos en usuarios para que operemeos con el en forma de diccionario
f = open('users.json')
usuarios = json.load(f)

#hasheo de contraseñas
for i in usuarios:
    passwordSinHashear = i['password']

    contraseña_hasheada = hashlib.sha256(passwordSinHashear.encode('utf-8')).hexdigest()

    i['password'] = contraseña_hasheada


#aqui te creo el archivo nuevo modificado con el nuevo diccionario que hemos modificado de usuarios
secureUsers = open('secure-users.json','a')
#el json se crea con toda su informacion pero con la sontraseña hasheada
#metemos los usuarioshasheados al archivo json que acabamos de crear
json.dump(usuarios, secureUsers)
