from tkinter import *
import time
root = Tk()
root.title("clock")
def get_time():
    string = time.strftime("%H:%M:%S:%p")
    label.config(text=string)
    label.after(1000,get_time)
label = Label(root, font=("Arial",50,"bold"), background="black", foreground="cyan")
label.pack()
get_time()
root.mainloop()
