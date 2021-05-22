#python program to read name and age of student
#check whether eligible for vote or not
name=input("enter name")
age=int(input("enter age"))
if age>=18:
	 print("Hello",name)
	 print("Elligible for vote")
else:
	 print("sorry!",name)
	 print("Not elligible for vote due to your age is",age)
	 
	 	 '''
	 	 output:1
	 	 enter name rajesh
	 	 enter age 19
	 	 Hello rajesh
	 	 Elligible for vote
	 	 
	 	output:2
	 	enter name rajesh
	 	enter age 16
	 	sorry! rajesh
	 	Not elligible for vote due to your age is 16
	  