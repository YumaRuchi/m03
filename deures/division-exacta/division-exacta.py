dividendo=int(input("Escriba el dividendo"))
divisor=int(input("Escriba el divisor"))
if divisor==0:
    print("No se puede dividir por 0")
else:
    if dividendo%divisor==0:
        print("La division es exacta. Cociente: ",dividendo/divisor,)
    else:
        if dividendo%divisor!=0:
            print("La division no es exacta. Cociente: ",dividendo/divisor,"Resto:",dividendo%divisor,)
