#In Centos 8
#sudo yum install python3-tkinter

import tkinter as tk
from tkinter import messagebox,Label,Entry

main_window = tk.Tk() #it gives main windows
main_window.title('My Calculator!')
#m = messagebox

l1= Label(main_window,text= 'First Value').grid(row=0)
l2= Label(main_window,text= 'Second Value').grid(row=1)

e1 = Entry(main_window)
e2 = Entry(main_window)

def add(a,b):
    if a != '' and b != '':
        return int(a)+int(b)
    return 0

def display():
    m = messagebox
    m.showinfo(title='Addition Result',message= "The result is "+ str(add(e1.get(),e2.get())))

#button = tk.Button(main_window,text='Get Value',width = 25,command=lambda : print(add(int(e1.get()),int(e2.get()))))
button = tk.Button(main_window,text='Get Value',width = 25,command=lambda : display())

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
button.grid(row=3,column=1)
main_window.mainloop()


