num1=int(input("escoje un numero"))
num2=int(input("escoje otro numero"))
if num1<=0 or num2 <=0:
    print("No puedes escoger un numero igual o inferior a 0")
else:
    if num1==num2:
        print("Son iguales")
    else:
        if num1>num2:
            res=num1%num2
            if res==0:
                print(num1,"es multiplo de",num2)
            else:
                print(num1,"no es multiplo de",num2)
        else:
            res=num2%num1
            if res==0:
                print(num2,"es multiplo de",num1)
            else:
                print(num2,"no es multiplo de",num1)
