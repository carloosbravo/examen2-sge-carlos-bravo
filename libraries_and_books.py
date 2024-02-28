import json
#nombreJson = open("libraries_and_books.json","w")

f = open('users.json')
usuarios = json.load(f)

libros = []
librerias = []

print(usuarios[0]["books"][0]["libraryId"])

#metemos los libros en una lista para tenerlos
for user in usuarios:
    libros.append(user['books'])
#creamos un diccionario con los libros

#ahora hay que meter los libros filtrandolo por el libraryId


