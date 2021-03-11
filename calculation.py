def docalculation(n,n1):
	print('you have two value so now tell me what ever you want to do')
	user=str(input('now tell me what ever you want to do '))
	if user=='add':
		print(n+n1)
	if user=='sub':
		print(n-n1)
	if user=='mult':
		print(n*n1)
num=int(input('enter the number '))
num2=int(input('enter the second number '))
docalculation(num,num2)