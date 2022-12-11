from tkinter import *
import tkinter.messagebox
def bt1():
    tkinter.messagebox.showinfo("hello", "Hello goodmorning")

def bt2():
    x = name.get()
    tkinter.messagebox.showinfo("your name", "Your name is "+x)




root = Tk()
root.title("INCOME AND EXPENSE TRACKER")
root.geometry("400x300")
HeadLabel = Label(root,text="Enter your name", fg="Blue", font=("Times",30)).place(x=70,y=30)
name = StringVar()
nameent = Entry(root, textvariable=name, font=("Times",25)).place(x=30,y=100)
loginbutton = Button(root, text="Login", height=2, width=10, bg="Cyan", command=bt1).place(x=80,y=180)
regbutton = Button(root, text="register", height=2, width=10, bg="Green", command=bt2).place(x=250,y=180) 

root.mainloop()
