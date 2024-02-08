






import random
secreto = random.randint(0, 100)
respuesta = -1
INTENTOS = 0
while respuesta != secreto and INTENTOS != 10:
respuesta = int(input("Intenta acertar: "))
if respuesta > secreto:
print("Es más PEQUEÑO que eso!")
INTENTOS += 1
elif respuesta < secreto:
print("Es más GRANDE que eso!")
INTENTOS += 1
if INTENTOS < 10:
print(f"Enhorabuena has acertado! El número era {secreto} y
has usado {INTENTOS} intentos.")
elif INTENTOS == 10:
print(f"Has fallado! El número era {secreto}, has gastado
{INTENTOS} intentos.")