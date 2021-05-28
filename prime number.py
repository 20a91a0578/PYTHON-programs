n=int(input("enter number:"))
count=0
i=1
while i<=n:
	if n%i==0:
		count+=1
		i+=1
	else:
		i+=1
		
if count==2:
	print('%d  is prime number'%(n))
else:
	print('%d is not a prime number'%(n))
		
'''
output:1
enter number:107
107 is prime number

output:2
enter number:98
98 is not a prime number
	'''