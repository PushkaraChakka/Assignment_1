1. Write a python program for the following:
– Input the string “Python” as a list of characters from console, delete at least 2 characters, reverse the
resultantstring and print it.


s='python'
# input string is taken as 's'
print (s)
# printing the input string
reversed1 = s[:-2]
# removing 2 characters from string
result1 = reversed1[::-1]
# reversing the string after removing characters
print (result1)
# printing the resultant string

– Take two numbers from user and perform at least 4 arithmetic operations on them.


s1=int(input('n1:')) # taking 1st input from user
s2=int(input('n2:')) # taking 2nd input from user
a1= s1+s2 # applying addition (+) operator on inputs
print(a1) # printing result of addition operator
a2= s1-s2 # subtraction (-)
print(a2) # printing result of subtraction
a3= s1*s2 # multiplication (*)
print(a3) # printing result of multiplication
a4= s1/s2 # division (/)
print(a4) # printing result of division


2. Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’.

s='I love playing with python' # taking input string
y=s.replace('python','pythons') # replacing the desired string
print(y) # printing the desired string


3. Use the if statement conditions to write a program to print the letter grade based on an input class score. Use the
grading scheme we are using in this class.


result=int(input('enter to check grade:')) # taking input from user
if(result>=90): # applying if condition
    print('grade is A')
elif(result>=80): 
    print('grade is B')
elif(result>=70):
    print('grade is C')
else:
    print("grade is Fail") # printing the grades according to the percentage