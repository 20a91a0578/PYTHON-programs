n=int(input())
if 1000<=n<2000:
	print('total bill is',n)
	print('Discount on billed amount is',(10*n)/100)
	print('paid bill is',n-(n*10)/100)
elif 2000<=n<3000:
	print('total bill is',n)
	print('Discount on billed amount is',(20*n)/100)
	print('paid bill is',n-(20*10)/100)
elif 3000<=n<5000:
	print('total bill is',n)
	print('Discount on billed amount is',(30*n)/100)
	print('paid bill is',n-(n*30)/100)		
elif n>5000:
	print('total bill is',n)
	print('Discount on billed amount is',(40*n)/100)
	print('paid bill is',n-(40*10)/100)	
else:
	print('you did not purchase enough to get discount' )
	print('paid bill is',n)
	'''
	output :1
	850
	you did not purchase enough to get discount
	
	output:2
	1000
	total bill is 1000
	discount on billed amount is 100
	paid bill is 900
	
	'''
