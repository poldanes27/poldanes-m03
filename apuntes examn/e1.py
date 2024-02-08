"""
Implementa un programa que demani un número i calculi el seu factorial .
El factorial d'un nombre és el producte de tots els enters entre 1 i el mateix nombre i es
representa pel nombre seguit d'un signe d'exclamació. Per exemple 5! = 1x2x3x4x5=
120)
"""

try:
num = int(input("Dame un num te hago factorial: "))
resultado = 1
for i in range(1, num +1):
resultado *= i

print(resultado)
except:
print("ERROR.")