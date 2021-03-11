def docalculation(n,n1):
	print('you have two value so now tell me what ever you want to do')
	user=str(input('now tell me what ever you want to do '))
	if user=='+':
		print(n+n1)
	elif user=='-':
		print(n-n1)
	elif user=='*':
		print(n*n1)
    elif user=="**":
        print(n**n1)
    elif user=="/":
        print(n/n1)
    elif user=="//":
        print(n//n1)
    elif user=="%":
        print(n%n1)
    else:
        print("wrong") 
num=int(input('enter the number '))
num2=int(input('enter the second number '))
docalculation(num,num2)