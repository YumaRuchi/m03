comprar_jamon=input("¿Has comprado jamon?")
abduccion=input("¿Te han abducido?")
dia_semana=input("Dia de la abduccion:")
estudiar=input("¿Has estudiado?")
if(comprar_jamon=="si")or((abduccion=="si")and(dia_semana=="jueves"))or(estudiar=="si"):
    print("Has aprobado")
else:
    print("Has suspendido")
