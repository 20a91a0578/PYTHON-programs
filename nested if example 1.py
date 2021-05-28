username=input()
if username=="CSEB":
	 password=input()
	 if password=="AEC":
	 	print('valid student')
	 else:
	 	print('invalid password')
else:
	print('invalid user name')

'''
Output:1
CSEB
AEC
valid student

output:2
CSEB
ABC
invalid password

output:3
CSEC
invalid username
'''
