def calcular_estadistiques(ruta_fitxer):
    with open(ruta_fitxer, 'r') as fitxer:
        notes = [int(nota) for nota in fitxer.read().split() if nota.isdigit()]

    if not notes:
        print("No s'han trobat notes vàlides a l'arxiu.")
        return None, None, None

    nota_minima = min(notes)
    nota_maxima = max(notes)
    nota_mitjana = sum(notes) / len(notes)

    return nota_minima, nota_maxima, round(nota_mitjana, 3)

ruta_fitxer = input("Introdueix la ruta de l'arxiu amb les notes dels estudiants: ")
nota_minima, nota_maxima, nota_mitjana = calcular_estadistiques(ruta_fitxer)

if nota_minima is not None:
    print("Nota mínima:", nota_minima)
    print("Nota màxima:", nota_maxima)
    print("Nota mitjana:", nota_mitjana)