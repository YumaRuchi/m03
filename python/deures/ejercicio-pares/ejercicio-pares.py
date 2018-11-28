#Lee un número del teclado
#Si es par: Escribe “Qué bonito número par”
#Si es impar: Escribe “Qué número más vulgar”
#Pista: usar módulo %
numero=int(input("Introduce un numero"))
if(numero%2==0):
    print("Qué bonito número par")
else:
    print("Qué número más vulgar")
