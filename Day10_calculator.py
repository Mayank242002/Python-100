def calculator(num1,num2,operation):
    if (operation=="+"):
        return num1+num2
    elif (operation=="-"):
        return num1-num2
    elif (operation=="*"):
        return num1*num2
    else:
        return num1/num2

choice="n"
flag1=0
flag2=1
while ((choice=="y") | (choice=="n")):
    if (flag1==1)|(flag2==1):
        num1=float(input("enter the first number?:"))
    print("+\n-\n*\n/\n")
    operation=input("Pick an Operation:")
    num2=float(input("what's the next number?:"))
    result=calculator(num1,num2,operation)
    print(num1,operation,num2," = ",result)

    choice=input("Type 'y' to continue calculating, or type 'n' to start a new calaculation:")
    if (choice=="n"):
        flag1=1
    else:
        num1=result
        flag1=flag2=0
      


       



