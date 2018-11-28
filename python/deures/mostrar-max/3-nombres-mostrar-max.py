num1=int(input("Introduce el primer numero"))
num2=int(input("Introduce el segundo numero"))
num3=int(input("Introduce el tercer numero"))
if num1>=num2 and num1>=num3:
    print("",num1,"")
else:
    if num2>=num3 and num2>=num1:
        print("",num2,"")
    else:
        if num3>=num2 and num3>=num1:
            print("",num3,"")
