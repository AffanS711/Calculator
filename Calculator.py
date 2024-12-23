import math
Start = input("Welcome to your personal calculator. Please write 's' to start!")
if Start == "s":
    Operation = input("Enter your operation. (a,m,d,s,sq)")
else: exit()
if Operation == 'a':
    Add = (input("Enter First Digit."))
    Add2 = (input("Enter Second Digit."))
    AddSum = float(Add) + float(Add2)
    print(AddSum)
if Operation == 'm':
    Mul = (input("Enter First Digit."))
    Mul2 = (input("Enter Second Digit."))
    MulSum = float(Mul) * float(Mul2)
    print(MulSum)
if Operation == 'd':
    Div = (input("Enter First Digit."))
    Div2 = (input("Enter Second Digit."))
    DivSum = float(Div) / float(Div2)
    print(DivSum)
if Operation == 's':
    Sub = (input("Enter First Digit."))
    Sub2 = (input("Enter Second Digit."))
    SubSum = float(Sub) - float(Sub2)
    print(SubSum)
if Operation == 'sq':
    SQ = (input("Enter First Digit."))
    SubSum = math.sqrt(float(SQ))
    print(SubSum)







