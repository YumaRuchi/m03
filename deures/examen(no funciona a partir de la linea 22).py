loteria=input("Has ganado la loteria?")
if loteria=="si":
    print("Cobras 3.000 euros netos")
else:
    me_caso=input("¿Te quieres casar con ese milloneti?")
    if me_caso=="si":
        edad=int(input("¿Que edad tiene?"))
        problemas_corazon=input("¿Tiene problemas del corazón?")
        casado=input("¿Está casado?")
        if edad>=80 and problemas_corazon=="si" and casado=="no":
            print("Estás de suerte, sueldo vitalicio en cuanto el viejo se muera")
        else:
            print("Todavía tienes una forma de cobrar 3.000€ al mes, a ver esas notas.")
            m01=int(input("¿Que nota sacaste en m01?"))
            m02=int(input("¿Que nota sacaste en m02?"))
            m03=int(input("¿Que nota sacaste en m03?"))
            m05=int(input("¿Que nota sacaste en m05?"))
            if m01>=9 and m02>=10 and m03>=8 and (m05>=6 and m05<=8):
                if m01*0.30+m02*0.40+m03*0.25+m05*0.05>8:
                    print("tu jefe te va a pagar 3.000€ netos al mes")
            else:
                print("Lo siento, tus notas no te van a hacer ganar ese dinero.")
