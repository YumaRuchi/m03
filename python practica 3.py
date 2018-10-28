dia_semana=input("¿En que dia de la semana estamos?")
clima=input("¿Cual es el clima actual?")
estacion=input("¿En que estacion del año estamos?")
hora=int(input("¿Que hora es?"))
temperatura=int(input("¿A cuantos grados estamos?"))
if(dia_semana=="Domingo"):
    print("Ponte el reloj de los domingos")
if(clima=="lluvia"):
    print("Ponte el sombrero")
if(clima=="soleado")and((hora>=13)and(hora<=16)):
    print("Ponte las gafas de sol")
if((estacion=="verano")and(((hora>=22)and(hora<=24))or((hora>=0)and(hora<=4)))and(temperatura<=17)):
    print("Ponte un pantalón largo")
else :
    print("Ponte pantalon corto")
