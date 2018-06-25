#Q1


f=open("new1.txt",encoding="utf8")
content=f.readlines()
print(content)
f.close()
n=int(input("enter the last line number from where u want to read: "))
while n>0:
 print(content[-n])
 n=n-1
 

#Q2


words=open("new1.txt","r",encoding="utf8").read().split()
print(words)
print(type(words))
uniqWords=sorted(set(words))
print(type(uniqWords))
for word in uniqWords:
 print(words.count(word),word)


#Q3



with open("lovey.txt","r",encoding="utf8") as f1:
 with open("new1.txt","w") as f2:
  for line in f1:
   f2.write(line)
   

#Q4



with open("lovey.txt","r",encoding="utf8") as f1:
   with open("new1.txt","r") as f2:
     for line1,line2 in zip(f1,f2):
       print(line1+line2)


#Q5



import random

with open("new1.txt", "w") as f:
    for i in range(10):
        numbers = str(random.randint(1, 100))
        f.writelines(numbers + '\n')
        print(numbers)

with open("new1.txt") as f1, open("lovey.txt", "w") as f2:
    numbers = f1.read().split()
    numbers.sort()
    print(numbers)
    for n in numbers:
        f2.write(n)
        f2.write("\n")
