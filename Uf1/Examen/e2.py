"""
Pol Danés
ASIXBc1
19-10-2023
"""
#Aqui creem totes las notes dels estudiants
primerestudiantr1 = float(input("Quina es la nota de Jaime de la r1?: "))
primerestudiantr2 = (float(input("Quina es la nota de Jaime de la r2?: ")))
segonestudiantr1 = float(input("Quina es la nota del Carlos de la r1?: "))
segonestudiantr2 = float(input("Quina es la nota de Carlos de la r2?: "))
tercerestudiantr1= float(input("Quina es la nota de Pol de la r1?: "))
tercerestudiantr2= float(input("Quina es la nota de Pol de la r2?: "))

#Aqui fem els calculs dels estudiants per saber la nota de la uf
calculprimer = (0.30 * primerestudiantr1) + (0.70 * primerestudiantr2)
calculsegon = (0.30*segonestudiantr1) + (0.70 * segonestudiantr2)
calcultercer = (0.30*tercerestudiantr1) + (0.370 * tercerestudiantr2)

#Aqui printem els resultats amb el calcul fet amb els 2 decimals amb la formula .2f
print (f"El jaime te un : {calculprimer:.2f}")
print (f"El Carlos te un : {calculsegon:.2f}")
print (f"El Pol te un : {calcultercer:.2f}")