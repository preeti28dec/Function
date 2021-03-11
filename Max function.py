def add(*num):
	num = [3,55,9,2,4,6,10]
	max=0
	i=0
	a=len(num)
	while i<a:
		if num[i]>max:
			max=num[i]
		i=i+1
	print(max)
add()