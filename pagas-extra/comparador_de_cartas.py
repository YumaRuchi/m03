#Cartas posibles: A 2 3 4 5 6 7 8 9 10 J Q K
carta1=str(input("Escoja la primera carta:"))
carta2=str(input("Escoja la segunda carta:"))
if (carta1=="A" or carta1=="2" or carta1=="3" or carta1=="4" or carta1=="5" or carta1=="6" or carta1=="7" or carta1=="8" or carta1=="9" or carta1=="10" or carta1=="J" or carta1=="Q" or carta1=="K") and (carta2=="A" or carta2=="2" or carta2=="3" or carta2=="4" or carta2=="5" or carta2=="6" or carta2=="7" or carta2=="8" or carta2=="9" or carta2=="10" or carta2=="J" or carta2=="Q" or carta2=="K"):
    if carta1=="A":
        print("La carta 1 gana!")
    if carta2=="A":
        print("La carta 2 gana!")
    else:
        if carta1>carta2:
            print("La carta 1 gana!")
        else:
            if carta2>carta1:
                print("La carta 2 gana!")
            else:
                if carta1==carta2:
                    print("Esto es un empate!")
else:
    print("La carta que has escogido no existe")
