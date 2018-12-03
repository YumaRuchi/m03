choice=int(input("Escoge cara[1] o cruz[2]"))
from random import randint
num=randint(1,2)
if num==1:
    print("Ha salido cara")
else:
    print("Ha salido cruz")
if num==choice:
    print("Has ganado")
else:
    print("Has perdido")
