#Q1
n=int(input("enter value :"))
if(n%4==0) :

	    print("leap year")

else :

      print("not a leap year")


#Q2


x=int(input("enter value of length :"))

y=int(input("enter value of breadth :"))

if(x==y) :

	print("dimension are of square")


else :

    print("dimension are of rectangle")



#Q3


x=int(input("enter age of x :"))


y=int(input("enter age of y :"))

z=int(input("enter age of z :"))

if x>y and x>z :

	    if y>z :

	    	print("x is older and z is younger")

	    else :
	    
	    	print("x is older and y is younger")


if y>z and y>x:

	if x>z:
		print("y is older and z is younger")

	else:
		print("y is older and x is younger")

if z>y and z>x :
        
        if y>x :

            print("z is older and x is younger")

        else :

            print("z is older and y is younger")

#Q4

p=int(input("enter points :"))

if p<=50 :

	    print("no prize")
elif p>=51 and p<=150:

	    print("wooden prize")

elif p>=151 and p<=180 :

	    print("book")

elif p>=181 and p<=200 :

	     print("chocolate")

else :   
	     print("invalid input")


#Q5


n=int(input("enter coat :"))

if n>=1000:

	    n=n-n*0.1
	    print(n)

else :  
        print(n)	    