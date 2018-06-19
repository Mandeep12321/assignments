# Q1

# using for loop

for i in range (0,10):
	n=int(input("enter an integer:"))
	print(n)
	
	
#Q2


i=1
while i!=-1:
	print("hello")
	i=i+1
	
	
#Q3



l=[]
s=[]
a=int(input("enter the range of list:"))
for x in range(a):
	l.append(int(input("enter a number:")))
for x in l:
	s.append(x**2)
print(l)
print(s)





#Q4

new_list=[]
list1=[]
list2=[]
list3=[]
for x in range(0,3):
	a=int(input("enter integer:"))
	new_list.append(a)

for x in range(3,6):
	a=str(input("enter a string:"))
	new_list.append(a)
	
	
for x in range(6,9):
	a=float(input("enter a float input:"))
	new_list.append(a)
	
print(new_list)

for x in new_list :
	if type(x)==int:
		list1.append(x)
	elif type(x)==str:
		list2.append(x)
	elif type(x)==float:
		list3.append(x)
print(list1)
print(list2)
print(list3)






#Q5


e=[]
o=[]


for i in range (1,101) :
	if i%2==0:
		e.append(i)
	else:
		o.append(i)
	i=i+1
print("odd list:")	
print(o)
print("even list:")
print(e)




#Q6

n=int(input("enter the number of row:"))
for i in range (0,n):
	for j in range (0,i+1):
		print("*",end="")
	print()
	
	
	
	#Q7

	

dict={}
x=int(input("enter the range of dictionary:"))
for i in range(x):
	keys=str(input("enter the key:"))
	values=input("enter the value:")
	dict[keys]=values
print("dictionary: ",end=""),print(dict)




#Q8




l[1]
a=int(input("enter the range of list:"))
for x in range(a):
 x=input("enter the number: ")
 l.append(x)
print(l)
y=input("select any number you want to search: ")
for x in l:
	if x==y:
		l.remove(x)
		print(l)
		break
if x!=y:
		print("element is not found")
		
	
