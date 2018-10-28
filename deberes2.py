#Els jubilats no paguen
#Els homes no jubilats paguen 1€
#Les dones no jubilades rosses no paguen
#Les altres paguen 0.5€

edad=int(input("¿Quina edat tens?"))
sexe=input("¿Quin es el teu sexe?")
cabells=input("¿De quin color tens els cabells?")
if (edad>=65) or ((sexe="dona") and (edad<65) and (cabells="rossos")):
         print("No pagas")
elif (sexe="home") and (edad<65):
         print("pagas 1€)
else:
         print("pagas 0.2€")
