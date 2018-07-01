#QUESTION:1 Write a python program using tkinter interface to write Hello World
#           and a exit button that closes the interface.
#SOLUTION:
import sys
import tkinter
from tkinter import *

def display():
	print("Hello Mandeep!")
	sys.exit()
root = Tk()
b=Button(root, text="EXIT", command=display)
b.pack()
root.mainloop()


#QUESTION:2 Write a python program to in the same interface as above
#           and create a action when the button is click it will display some text. 
#SOLUTION:
import tkinter
from tkinter import *

def display():
	print("Hello Mandeep!")
	
root=Tk()
b=Button(root,text="click",width=25,bg='blue',fg='white',command=display)
b.pack()
root.mainloop()


		   
#QUESTION:3 Create a frame using tkinter with any label text and two buttons.
#           One to exit and other to change the label to some other text.
#SOLUTION:
import tkinter
from tkinter import *
import sys
def Change():
	label.config(text= "ram and sham")
root = Tk()
label = Label(root,text="hello friends")
label.grid(row = 0)
btn = Button(root, text="Change",command=Change)
btn.grid(row= 1)
btn2 = Button(root, text="Exit",command=sys.exit)
btn2.grid(row= 2)
root.mainloop()


#QUESTION:4 Write a python program using tkinter interface to take an input in the GUI program and print it.
#SOLUTION:
import tkinter
from tkinter import *

def show():
	print(entry.get())
	
root=Tk()
root.title("My App")
root.geometry("250x250")
root.resizable(True,True)
root.minsize(200,200)
entry=Entry(root,width=20)
entry.pack()
b=Button(root,text='click',width=20,command=show)
b.pack()
root.mainloop()