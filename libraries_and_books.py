import json
#nombreJson = open("libraries_and_books.json","w")

f = open('users.json')
usuarios = json.load(f)

print(usuarios[1])
print(usuarios[1]['userName'])
#creamos un diccionario con los libros
libros = {}

for item in usuarios:
    libros[usuario[] =

print(libros)


