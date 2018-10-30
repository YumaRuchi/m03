#Lee la edad del teclado
#Si tiene entre 18 y 23 años (ambos incluídos) le decimos que puede entrar en la sesión de jóvenes.
edad=int(input("¿Que edad tienes?"))
if (edad>=18 and edad<=23):
    print("Puedes entrar a la sesión de jóvenes")
else:
    print("No puedes entrar a la sesión de jóvenes")
