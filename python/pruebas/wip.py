print("¿Que desea hacer el amo?")
print("S:-Salir")
for opciones in range(0,5):
    if opciones+1==2:
        print("1.-Sumar")
    if opciones+1==3:
        print("2.-Restar")
    if opciones+1==4:
        print("3.-Multiplicar")
    if opciones+1==5:
        print("4.-Dividir")
seleccion=input()
if seleccion=="S"or seleccion=="1"or seleccion=="2"or seleccion=="3"or seleccion=="4":
    print ("buenisima")
