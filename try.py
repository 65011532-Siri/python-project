from tkinter import Tk
from tkinter.ttk import Button
from functools import partial
  
  
# Demo function 1
def fun1():
    print("Function 1")
  
  
# Demo function 2
def fun2(x):
    print("Hello")
    print(x)
  
  
if __name__ == "__main__":
    # Creating top-level window
    master = Tk()
  
    # Setting window title
    master.title("Bind multiple function to Button")
  
    # Setting window Dimensions
    master.geometry("400x250")
    a = 3
    # Creating a button with more than one command using lambda
    button = Button(master, text="Button", command=lambda: [fun1(), partial(fun2, a)])
  
    # Attaching button to the top-level window
    # Always remember to attach your widgets to the top-level
    button.pack()
  
    # Mainloop that will run forever
    master.mainloop()