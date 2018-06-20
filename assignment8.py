#Q1


#Many of Python's time functions handle time as a tuple of 9 numbers, as shown below −
# Index	Field	Values
# 0	4-digit year	2008
# 1	Month	1 to 12
# 2	Day	1 to 31
# 3	Hour	0 to 23
# 4	Minute	0 to 59
# 5	Second	0 to 61 (60 or 61 are leap-seconds)
# 6	Day of Week	0 to 6 (0 is Monday)
# 7	Day of year	1 to 366 (Julian day)
# 8	Daylight savings	-1, 0, 1, -1 means library determines DST
 

#Q2


import time
print(time.asctime(time.localtime(time.time())))


#Q3 

from datetime import datetime
print (datetime.now().strftime("%m"))


#Q4



from datetime import datetime
print(datetime.now().strftime("%a"))


#Q5



from datetime import datetime
print(datetime.now().strftime("%d"))



#Q6
import time 
print(time.localtime())


#Q7


import math
print(math.factorial(int(input("enter any number: "))))


#Q8


x=int(input("enter a number: "))
y=int(input("enter an another number: "))
import math
print(math.gcd(x,y))


#Q9


import os
print(os.getcwd)

#2. Get the user environment.


import os
print(os.environ)
