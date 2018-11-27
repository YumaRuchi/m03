tipo_gasolina=int(input("Preguntamos al usuario que tipo de gasolina quiere:\n-Super: Normal(1.5€)[1], Turbo(1.55€)[2]\n-Sin plomo: Normal(1.6€)[3], Con aditivos(sabor naranja)(1.65€)[4]\n-Diesel: Normal(1.7€)[5], Fast&Furius(1.75€)[6]"))
litros=int(input("¿Cuantos litros quieres?"))
if tipo_gasolina==1:
	tipo_gasolina=1.5
	print("El importe es de",tipo_gasolina*litros,".")
if tipo_gasolina==2:
	tipo_gasolina=1.55
	print("El importe es de",tipo_gasolina*litros,".")
if tipo_gasolina==3:
	tipo_gasolina=1.6
	print("El importe es de",tipo_gasolina*litros,".")
if tipo_gasolina==4:
	tipo_gasolina=1.65
	print("El importe es de",tipo_gasolina*litros,".")
if tipo_gasolina==5:
	tipo_gasolina=1.7
	print("El importe es de",tipo_gasolina*litros,".")
if tipo_gasolina==6:
	tipo_gasolina=1.75
	print("El importe es de",tipo_gasolina*litros,".")
