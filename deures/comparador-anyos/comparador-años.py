anyo_actual=int(input("¿En que año estamos?"))
anyo_cualquiera=int(input("Escribe un año cualquiera"))

if anyo_actual==anyo_cualquiera:
    print("Son el mismo año!")
else:
    if anyo_actual>anyo_cualquiera:
        print("Han pasado",anyo_actual-anyo_cualquiera,"años desde",anyo_cualquiera,".")
    else:
        if anyo_actual<anyo_cualquiera:
            print("faltan",anyo_cualquiera-anyo_actual,"para el año",anyo_cualquiera,".")
