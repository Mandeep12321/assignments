#Q


#SOLUTION:
#in above code there is an indentation error in line if a<4: and print(a).after resolving the 
#indentation error the code give the output which is ZeroDivisionError
a=3
if a<4:
 a=a/(a-3)
 print(a)
#OUTPUT:ZeroDivisionError: division by zero
# after handling
try:
 a=3
 if a<4:
  a=a/(a-3)
  print(a)
except Exception:
  print("Exception occur")
  

#Q2


l=[1,2,3]
print(l[3])
#SOLUTION: 
#The output of the above code is IndexError: list index out of range
try:
 l=[1,2,3]
 print(l[3])
except Exception:
 print("Exception occur")
 

#Q3


#SOLUTION:
# In above code there is an error in print-Missing parentheses in call to 'print'.
# after solving this error the code is:
try:
    raise NameError("Hi there") 
except NameError:
    print("An exception")
    raise
# The Exception was raised and the output is 
#                     raise NameError("Hi there")  # Raise Error
#                     NameError: Hi there   


#Q4
 # Function which returns a/b
# def AbyB(a , b):
	# try:
		# c = ((a+b) / (a-b))
	# except ZeroDivisionError:
		# print "a/b result in 0"
	# else:
		# print c

# Driver program to test above function
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)
#SOLUTION: 
# In above code there is an error in print statements which is of missing parentheses which is
 # support in python2 not in python3.After removing the error from print statements the code is:
 
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)		
# and the output is 
# -5.0
# a/b result in 0


#Q5


#SOLUTION:
import club
 print("hello world")
 
#after handling
try:
 import club
 print("hello world")
except Exception:
 print("Exception occured")
 

#2. Value Error
#SOLUTION:

n=int(input("Enter a number: ") 
print("number is ",n)

# after handling
try:
 n=int(input("Enter a number: "))
 print("number is ",n)
except Exception:
 print("Exception occur for value error")
 
 
#3. Index Error
#SOLUTION:
l=[1,2,3]
print(l[3])
#The output of the above code is IndexError: list index out of range
#after handling

try:
 l=[1,2,3]
 print(l[3])
except Exception:
 print("Exception occur")


#Q6


#SOLUTION:
class AgeTooSmallError(Exception):
 pass
a=1
while True:
  
 print("you have to enter the age 18 or more than 18")
 try:
  a=int(input("enter the age:"))
  if a<18:
   raise  AgeTooSmallError()
  print("Correct")
  break
     
 except Exception:
   print("Incorrect Age")
   
