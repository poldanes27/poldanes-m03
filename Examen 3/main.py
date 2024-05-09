"""
Pol Danes
"""
import os

try:
    #Crea fitxers amb paraules de x longituds
    def crear_fitxers(fitxer_entrada, directori_sortida):
        with open(fitxer_entrada, 'r') as fitxer:
            paraules = fitxer.read().split()

        # Si el directori de sortida no existeix, el crea
        if not os.path.exists(directori_sortida):
            os.makedirs(directori_sortida)

        # Per a cada longitud de paraula especificada, crea un fitxer amb paraules d'aquella longitud
        for longitud in [2, 4, 6, 8, 9]:
            fitxer_sortida = os.path.join(directori_sortida, f"paraules-{longitud}.txt")
            with open(fitxer_sortida, 'w') as fitxer:
                paraules_seleccionades = [paraula for paraula in paraules if
                                          len([char for char in paraula if char.isalnum()]) == longitud]
                fitxer.write('\n'.join(paraules_seleccionades))

    #Arxiu d'entrada i directori de sortida per a la funció crear_fitxers
    fitxer_entrada = 'paraules.txt'
    directori_sortida = 'Javi - SUSANA AQUI ESTAN ELS FITXERS'
    # Crida la funció crear_fitxers amb els paràmetres especificats
    crear_fitxers(fitxer_entrada, directori_sortida)

    #Funio que compta la quantitat de vocals en una paraula
    def numero_vocals(paraula):
        vocals = "aeiouAEIOU"
        quantitat_vocals = sum(1 for lletra in paraula if lletra in vocals)
        return quantitat_vocals
    #funció que crea la copia del fitxer
    def crear_copia_vocals(fitxer_entrada, fitxer_sortida):
        with open(fitxer_entrada, 'r') as fitxer:
            paraules = fitxer.read().split()
        with open(fitxer_sortida, 'w') as fitxer:
            for paraula in paraules:
                quantitat_vocals = numero_vocals(paraula)
                fitxer.write(f"{quantitat_vocals}\t{paraula}\n")

    #Arxius d'entrada i sortida'
    input_file = 'paraules.txt'
    output_file = 'paraulesquantitatvocals.txt'
    #Crida la funció crear_copia_vocals amb els arxius d'entrada i sortida especificats
    crear_copia_vocals(input_file, output_file)

except:
    print("Algo ha sortit malament")