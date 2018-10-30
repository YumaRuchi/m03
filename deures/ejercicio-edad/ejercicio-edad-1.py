#Lee la edad del teclado
#Si tiene entre 15 y 17 años (ambos incluídos) le decimos que puede entrar en la sesión de tarde.
edad=int(input("¿Que edad tienes?"))
if (edad>=15 and edad<=17):
    print("Puedes entrar a la sesión de tardes")
else:
    print("No puedes entrar a la sesión de tardes")
