def main():
    num_llibres = int(input("Introdueix el nombre de llibres: "))

    llibres = []
    llibre_mes_curt = None
    llibre_mes_llarg = None

    for _ in range(num_llibres):
        titol = input("Introdueix el títol del llibre: ")
        autor = input("Introdueix l'autor del llibre: ")
        pagines = int(input("Introdueix el nombre de pàgines del llibre: "))

        llibre = (titol, autor, pagines)
        llibres.append(llibre)

        if llibre_mes_curt is None or pagines < llibre_mes_curt[2]:
            llibre_mes_curt = llibre

        if llibre_mes_llarg is None or pagines > llibre_mes_llarg[2]:
            llibre_mes_llarg = llibre

    with open("books.out", "w") as fitxer:
        fitxer.write("Llibres\n")
        fitxer.write("------------\n")

        for llibre in llibres:
            fitxer.write(f"{llibre[0]} - {llibre[1]} - {llibre[2]} pàgines\n")

        fitxer.write("------------\n")
        fitxer.write(f"Total: {num_llibres} llibres\n")
        fitxer.write(f"Llibre més curt: {llibre_mes_curt[0]} - {llibre_mes_curt[1]} - {llibre_mes_curt[2]} pàgines\n")
        fitxer.write(
            f"Llibre més llarg: {llibre_mes_llarg[0]} - {llibre_mes_llarg[1]} - {llibre_mes_llarg[2]} pàgines\n")

main()