#Q1

def area():
	x=int(input("enter radius of circle:"))
	z=3.14*x**2
	print("area of circle is",z)
area()



#Q2
def perfect(n):
# for adding the divisors use 'sum' variable.
	sum=0
	for i in range(1,n-1):
		if n%i==0:
			sum =sum+i
	if sum==n:
		print(sum)
for i in range(1001):
	perfect(i)
	

#Q3

def rec(i,n):
	x=0
	if i>10:
		return 0
	else:
		x=n*i
		
		print("%d * %d = %d"%(n,i,x))
		rec(i=i+1,n=n)
		
rec(n=12,i=1)



#Q4



def power():
	x=int(input("enter the first number:"))
	y=int(input("enter the second number:"))
	z=x**y
	print("the final value is ",z)
power()



#Q5


def fact(n):

	if n==1 or n==0:
			return 1
	else:
		return(n*fact(n-1))
		
n=int(input("enter a number"))
print("the factorial of %d:"%n,fact(n))
	
c=fact(n)
d={n:c}
print(d)	
