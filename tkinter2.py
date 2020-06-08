#In Centos 8
#sudo yum install python3-tkinter

import tkinter as tk
from tkinter import *

main_window = tk.Tk() #it gives main windows
main_window.title('My Gender!')

var1 = IntVar()
var2 = IntVar()
c= tk.BooleanVar()
button1 = tk.Checkbutton(main_window,text='Male',onvalue = True,offvalue = False,variable = c,command=lambda : print(c.get()))
#button2 = tk.Checkbutton(main_window,text='Female',onvalue = 1,offvalue = 0,variable = var2)
button1.pack()
#button2.pack() #packing means putting all widgets on window, grid(), place()
main_window.mainloop()


