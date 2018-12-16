from random import randint
import time
intentos=3
num=randint(1,10)
while intentos>0:
    print("Tienes",intentos,"intentos.")
    eleccion=int(input("Escoge un número del 1 al 10."))
    if eleccion==num:
        print("Has acertado, toma 100€")
        intentos=-1
    else:
        print("Lo siento, no has acertado.")
        intentos=intentos-1
if intentos==0:
    print("Te has quedado sin intentos")
