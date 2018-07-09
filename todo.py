import tkinter
from tkinter import *


root=Tk()
root.title("To-Do")                
root.config(bg="lightblue")
root.geometry("480x480")
root.resizable(FALSE,FALSE)

list1=[]
f=StringVar()

#######################     functions      ##################################
def add():
    global f,serial,list1
    serial=len(list1)
    f=e.get()
    if not f=="":
        list1.append(f)
        Lb.insert(END,' '.join((str(serial + 1),list1[-1])))
        e.delete(0, END)
    else:
        pass


def delete_all():
    Lb.delete(0, END)
    list1.clear()


def delete():
    f=e.get()
    for i in list1:
        if i==f:
            Lb.delete(0, END)
            list1.remove(f)
            for j in range (len(list1)):
                Lb.insert(END,' '.join((str(j+1),list1[j])))
            e.delete(0,END)
        else:
            pass

def sort_asc():
    list1.sort()
    Lb.delete(0, END)
    for i in range (len(list1)):
        Lb.insert(END,' '.join((str(i+1),list1[i])))
    e.delete(0,END)


def sort_dsc():
    list1.sort()
    list1.reverse()
    Lb.delete(0,END)
    for i in range (len(list1)):
        Lb.insert(END,' '.join((str(i+1),list1[i])))
    e.delete(0,END)




choose_lable=Label(root,text="",bg="skyblue")
choose_lable.grid(row=3,column=0)

label=Label(root,text="To-Do List",pady=10)
label.grid(row=0,column=0)


add_button=Button(root,text="Add item",command=add,bd='3',bg="black",fg="white",width=15,height=1)
add_button.grid(row=1,column=0)

clr_button=Button(root,text="Clear all tasks",command=delete_all,bd='3',bg="black",fg="red",width=15,height=1)
clr_button.grid(row=2,column=0)

remove_button=Button(root,text="Remove",command=delete,bd='3',bg="black",fg="white",width=15,height=1)
remove_button.grid(row=3,column=0)

asc_button=Button(root,text="sort(desc)",bd='3',command=sort_asc,bg="black",fg="red",width=15,height=1)
asc_button.grid(row=4,column=0)

sort_button=Button(root,text="Sort(DESC)",command=sort_dsc,bd='3',bg="black",fg="white",width=15,height=1)
sort_button.grid(row=5,column=0)




exit_button=Button(root,text="Exit",command=root.destroy,bg="red",bd='3',width=15,height=1)
exit_button.grid(row=8,column=0)


e=Entry(root,width=40,textvariable=f)
e.place(x=180,y=45)

Lb=Listbox(root,width=40,height=18)
Lb.place(x=180,y=100)

root.mainloop()