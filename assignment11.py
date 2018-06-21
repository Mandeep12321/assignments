#Q1




import threading
from threading import Thread
import time


def display():
    for x in range(2):
      print(threading.current_thread().getName(),":","dhiman")
      time.sleep(5)

t=Thread(target=display)
t.start()


#Q2





import threading
from threading import Thread
import time

def display():
    for x in range(1,11):
      print(x)
      time.sleep(1)

t=Thread(target=display)
t.start()


#Q3




import threading
from threading import Thread
import time
def display(l):
    t=2
    for x in l:
        print(x)
        time.sleep(t)
        t=t+2
l=[2,3,6,9,1]
t3=Thread(target=display,args=(l,))
t3.start()


#Q4



import threading
from threading import Thread
import time
import math
def fact():
     fact=1
     for x in range(1,num+1):
         fact=fact*x
     print("The factorial of",num,"is",fact)

num=int(input("Enter any  number: "))
t4=Thread(target=fact)
t4.start()
