n=int(input('enter number:'))
temp=n
sum=0
r=0
while n!=0:
  r=n%10
  sum=sum*10+r
  n=n//10
print('Reverse of %d  is %d'%(temp,sum))

'''
output:
	enter number:64782
	Reverse of 64782 is 28746
	'''
	