#Lee un número del teclado
#Si es:
#-par
#-entre -10 y 40
#-negativo
#Nota: una sola condició
numero=float(input("Escribe un numero:"))
if numero>=-10 and numero<=40:
    pos="Está entre el -10 y el 40"
else:
    pos="No está entre el -10 y el 40"
if numero%2==0:
    PI="Es par"
else:
    PI="Es inpar"
if numero<0:
    NP="Es negativo"
else:
    NP="Es positivo"
print("Datos sobre el número:\n-",pos,"\n-",PI,"\n-",NP,)
