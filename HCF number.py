def HCF(a,b):
    if (b==0):
        return (a)
    else:
        return HCF(b,a%b)
a=int(input("enter the first number "))
b=int(input("enter the second number "))
print("that is HCF value",HCF(a,b))