import random

random_num = random.randint(1, 100)
print(random_num)

attempt = 1
num = int(input("Escribe un numero: "))

while num != random_num and attempt != 3:
    if num < random_num:
        print(f"El numero a adivinar es mas grande te quedan {10-attempt} intentos")
    else:
        print(f"El numero a adivinar es mas pequeño que el que has puesto te quedan {10-attempt} intentos")
    print()
    num = int(input("Escribe un numero: "))
    attempt += 1
if num == random_num:
    print(f"Has adivinado el numero has usado {attempt} intentos")
else:
    print(f"has llegado al limite de intentos. El numero era {random_num}")