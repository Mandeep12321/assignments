#Q1

t=(1,2,3,4)
print(t)

print(len(t))

#Q2

print(max(t))

print(min(t))


#Q3
t=(1,2,3)
p=1
p=p*t[0] # p = 1 * 1
p=p*t[1] # p = 1 * 2
p=p*t[2] # p = 2 * 3
#p=6
print(p)

#sets


#Q1:


a=int(input("enter value"))
b=int(input("enter value"))
c=int(input("enter value"))
d=int(input("enter value"))

s=set([a,b,c,d])
print(s)


#1

s2=set([11,22,33,44])

print(s-s2)

#2  union


print(s|s2)


#3 intersection

print(s & s2)


# dictionary


#Q1


a=input("enter name of student :")
aa=int(input("enter marks :"))
b=input("enter name of student :")
ab=int(input("enter marks :"))
c=input("enter name of student :")
ac=int(input("enter marks :"))
d=input("enter name of student :")
ad=int(input("enter marks :"))
e=input("enter name of student :")
ae=int(input("enter marks :"))
f=input("enter name of student :")
af=int(input("enter marks :"))
g=input("enter name of student :")
ag=int(input("enter marks :"))
h=input("enter name of student :")
ah=int(input("enter marks :"))
i=input("enter name of student :")
ai=int(input("enter marks :"))
j=input("enter name of student :")
aj=int(input("enter marks :"))

d={a:aa,b:ab,c:ac,d:ad,e:ae,f:af,g:ag,h:ah,i:ai,j:aj}

print(d)


#Q2

value_list=list(d.values())
value_list.sort()
print(value_list)


#Q3

l=list("mississippi")

d={}

d['m']=l.count('m')


d['s']=l.count('s')
4