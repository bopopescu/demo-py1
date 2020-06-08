#In Centos 8
#sudo yum install python3-tkinter

import tkinter as tk

main_window = tk.Tk() #it gives main windows
main_window.title('My Calculator!')

button = tk.Button(main_window,text='MyName',width = 25,command = main_window.destroy)

button.pack() #packing means putting all widgets on window, grid(), place()
main_window.mainloop()


