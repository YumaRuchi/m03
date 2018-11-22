#cada 30 dias canviar de mes
print("enero")
for dia in range(0,365):
    print(dia+1)
    if dia%365==30-1:
        print("febrero")
    if dia%365==60-1:
        print("marzo")
    if dia%365==90-1:
        print("abril")
    if dia%365==120-1:
        print("mayo")
    if dia%365==150-1:
        print("junio")
    if dia%365==180-1:
        print("julio")
    if dia%365==210-1:
        print("agosto")
    if dia%365==240-1:
        print("septiembre")
    if dia%365==270-1:
        print("octubre")
    if dia%365==300-1:
        print("novembre")
    if dia%365==330-1:
        print("desembre")
    if dia%365==360-1:
        print("?¿?")
