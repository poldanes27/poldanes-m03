'''
Pol Danés
ASIXBc1
19-10-2023
'''
import math
#Demanem la alçada  i la amplanda i las guarde,
alçada= int(input("Quina es l'alçada del camp?"))
amplada= int(input("Quina es la amplada del camp"))
#Aqui fem el calcul de la arrerl cuadrada amb la operacio de math.sqrt
diagonal = math.sqrt((alçada*alçada)+(amplada*amplada))

print("La Diagonal del camp es :", diagonal)
