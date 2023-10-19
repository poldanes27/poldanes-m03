'''
Alejo Liébana
Pol Danés
ASIXBc1
18-10-2023

EOP 2
Expliqueu que passa a:
adn = "ATGAACTGTGC"
adn=adn.replace('A', 'a')
adn=adn.replace('T', 'A')
adn=adn.replace('a', 'T')
'''

adn = "ATGAACTGTGC"
#Cambia todas las A por a y nos da "aTGaaCTGTGC"
adn=adn.replace('A', 'a')
#Cambia las T por A y nos da "aAGaaCAGAGC"
adn=adn.replace('T', 'A')
#Cambia las a por T y nos da "TAGTTCAGAGC"
adn=adn.replace('a', 'T')
#Al final se han intercambiado las A por T
print(adn)