pregunta_inicial=input("¿Quieres calcular el area de un triangulo o la de un circulo? (escribe T o C)")
if pregunta_inicial=="T" or pregunta_inicial=="C":
    if pregunta_inicial=="T":
        base=float(input("¿Cual es la base del triangulo?"))
        altura=float(input("¿Cual es la altura del triangulo?"))
        print("Un triangulo de base",base,"y altura",altura,"tiene un area de",base*altura/2,".")
    else:
        radio=float(input("¿Cual es el area del circulo?"))
        print("Un circulo de radio",radio,"tiene un area de",3.141592*(radio*radio),".")
else:
    print("No has introducido una opción válida.")
