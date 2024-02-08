import unicodedata

try:
    palabra = input("Escoje una palabra: ")
    palabra_limpia = ''.join(c for c in unicodedata.normalize('NFD', palabra) if unicodedata.category(c) != 'Mn')
    palabra_limpia = palabra_limpia.lower()
    if palabra_limpia == palabra_limpia[::-1]:
        print("La palabra es igual")
    else:
        print("La palabra no es igual ")
except:
    print("Error al introducir la palabra")