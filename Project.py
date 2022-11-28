import datetime 
import numpy as np
from tkinter import *
import tkinter.messagebox


class Acc:
    def __init__ (self,accname):
        self.name = accname
        self.bankdatabase = np.zeros((1,13), dtype="float32")
        self.cashdatabase = np.zeros((1,13), dtype="float32")
        np.savetxt(self.name+"_bankdatabase.txt", self.bankdatabase, fmt="%f")
        np.savetxt(self.name+"_cashdatabase.txt", self.cashdatabase, fmt="%f")


    def report(self):
        print("1.Bank Account or 2.Cash")
        a = int(input())
        if a == 1:
            print("Bank Account")
            print("total balance =", self.bankdatabase[0,-1])
            print("total income =", self.bankdatabase[0,-2])
            print("Total expenses =", self.bankdatabase[0,-3])
        elif a == 2: 
            print("Cash")
            print("total balance =", self.cashdatabase[0,-1])
            print("total income =", self.cashdatabase[0,-2])
            print("Total expenses =", self.cashdatabase[0,-3])

    def income(self):
        date = dateinput()
        print("1.Bank Account or 2.Cash Account")
        a = int(input())
        b = float(input("Amount of money: "))
        if a == 1:
            self.bank_income_category(b,date)
        elif a == 2:
            self.cash_income_category(b,date)


    def expense(self):
        date = dateinput()
        print("1.Bank Account or 2.Cash Account")
        a = int(input())
        b = float(input("Amount of money: "))
        if a == 1:
            self.bank_expense_category(b,date)
        elif a == 2:
            self.cash_expense_category(b,date)

    def bank_income_category(self, amount, date):
        print("1.Salary 2.Incoming Transfer 3.other")
        cate = int(input())
        if cate == 1:
            self.bankdatabase = np.append(self.bankdatabase, [[date,0,0,0,0,0,0,amount,0,0,0,0,0]], axis=0)
        if cate == 2: 
            self.bankdatabase = np.append(self.bankdatabase, [[date,0,0,0,0,0,0,0,amount,0,0,0,0]], axis=0)
        if cate == 3:
            self.bankdatabase = np.append(self.bankdatabase, [[date,0,0,0,0,0,0,0,0,amount,0,0,0]], axis=0)

    def cash_income_category(self, amount, date):
        print("1.Salary 2.Incoming Transfer 3.other")
        cate = int(input())
        if cate == 1:
            self.cashdatabase = np.append(self.cashdatabase, [[date,0,0,0,0,0,0,amount,0,0,0,0,0]], axis=0)
        elif cate == 2: 
            self.cashdatabase = np.append(self.cashdatabase, [[date,0,0,0,0,0,0,0,amount,0,0,0,0]], axis=0)
        elif cate == 3:
            self.cashdatabase = np.append(self.cashdatabase, [[date,0,0,0,0,0,0,0,0,amount,0,0,0]], axis=0)

    def cash_expense_category(self, amount, date):
        print("1.Food and Beverage 2.Transportation and gas 3.Entertainment 4.Sport 5.Investment 6.other")
        cate = int(input())
        if cate == 1:
            self.cashdatabase = np.append(self.cashdatabase, [[date,amount,0,0,0,0,0,0,0,0,0,0,0]], axis=0)
        elif cate == 2: 
            self.cashdatabase = np.append(self.cashdatabase, [[date,0,amount,0,0,0,0,0,0,0,0,0,0]], axis=0)
        elif cate == 3:
            self.cashdatabase = np.append(self.cashdatabase, [[date,0,0,amount,0,0,0,0,0,0,0,0,0]], axis=0)
        elif cate == 4: 
            self.cashdatabase = np.append(self.cashdatabase, [[date,0,0,0,amount,0,0,0,0,0,0,0,0]], axis=0)
        elif cate == 5:
            self.cashdatabase = np.append(self.cashdatabase, [[date,0,0,0,0,amount,0,0,0,0,0,0,0]], axis=0)
        elif cate == 6:
            self.cashdatabase = np.append(self.cashdatabase, [[date,0,0,0,0,0,amount,0,0,0,0,0,0]], axis=0)

    def bank_expense_category(self, amount, date):
        print("1.Food and Beverage 2.Transportation and gas 3.Entertainment 4.Sport 5.Investment 6.other")
        cate = int(input())
        if cate == 1:
            self.bankdatabase = np.append(self.bankdatabase, [[date,amount,0,0,0,0,0,0,0,0,0,0,0]], axis=0)
        elif cate == 2: 
            self.bankdatabase = np.append(self.bankdatabase, [[date,0,amount,0,0,0,0,0,0,0,0,0,0]], axis=0)
        elif cate == 3:
            self.bankdatabase = np.append(self.bankdatabase, [[date,0,0,amount,0,0,0,0,0,0,0,0,0]], axis=0)
        elif cate == 4: 
            self.bankdatabase = np.append(self.bankdatabase, [[date,0,0,0,amount,0,0,0,0,0,0,0,0]], axis=0)
        elif cate == 5:
            self.bankdatabase = np.append(self.bankdatabase, [[date,0,0,0,0,amount,0,0,0,0,0,0,0]], axis=0)
        elif cate == 6:
            self.bankdatabase = np.append(self.bankdatabase, [[date,0,0,0,0,0,amount,0,0,0,0,0,0]], axis=0)


    def update_bankdatebase(self):
        self.bankdatabase[0,-3] = np.sum(np.sum(self.bankdatabase, axis=0)[1:7], axis=0)
        self.bankdatabase[0,-2] = np.sum(np.sum(self.bankdatabase, axis=0)[7:10], axis=0)
        self.bankdatabase[0,-1] = self.bankdatabase[0,-2] - self.bankdatabase[0,-3]
        self.cashdatabase[0,-3] = np.sum(np.sum(self.cashdatabase, axis=0)[1:7], axis=0)
        self.cashdatabase[0,-2] = np.sum(np.sum(self.cashdatabase, axis=0)[7:10], axis=0)
        self.cashdatabase[0,-1] = self.cashdatabase[0,-2] - self.cashdatabase[0,-3]
        np.savetxt(self.name+"_bankdatabase.txt", self.bankdatabase, fmt="%f")
        np.savetxt(self.name+"_cashdatabase.txt", self.cashdatabase, fmt="%f")

        

def dateinput(x = datetime.datetime.now()):
    print("Select date: 1.Today 2.customs day")
    i = int(input())
    if i == 2:
        print("Enter date: ")
        dd = int(input())
        print("Enter month: ")
        mm = int(input())
        print("Enter year(20xx): ")
        yy = int(input())
        x = datetime.datetime(yy, mm, dd)
    x = str(x.year)+str(x.month)+str(x.day)
    return float(x)

class oldAcc(Acc):
    def __init__(self,accname):
        self.name = accname
        self.bankdatabase = np.loadtxt(self.name+"_bankdatabase.txt")
        self.cashdatabase = np.loadtxt(self.name+"_cashdatabase.txt")
        if np.ndim(self.bankdatabase) == 1:
            self.bankdatabase = self.bankdatabase.reshape(1,13)
        if np.ndim(self.cashdatabase) == 1:
            self.cashdatabase = self.cashdatabase.reshape(1,13)


def addbutton():
    x = cate


def login():
    name = nameinput.get()
    name = str(name)
    p = True
    file = open("acc_database.txt", "r")
    b = len(file.readlines())
    for i in range(b):
        file = open("acc_database.txt", "r")
        a = file.readlines()[i]
        a = a.strip("\n")
        if name == a:
            acc_name = oldAcc(name)
            p = False
            root.destroy()
            mainpage(acc_name)
            break
    if p == True:
        tkinter.messagebox.showinfo("Your name is not found", "Your name is not found. \nPlaese register first")
        
def register():
    name = nameinput.get()
    name = str(name)
    p = True
    file = open("acc_database.txt", "r")
    b = len(file.readlines())
    file = open("acc_database.txt", "r")
    accdata = file.readlines()
    for i in range(b):
        file = open("acc_database.txt", "r")
        a = file.readlines()[i]
        a = a.strip("\n")
        if name == a:
            tkinter.messagebox.showinfo("Already have account", "Your name has already register \nPlease login")
            break
    if p == True:
        acc_name = Acc(name)
        accdata.append(name+"\n")
        datafile = open("acc_database.txt", "w")
        k = datafile.writelines(accdata)
        datafile.close()
        root.destroy()
        mainpage(acc_name)

def mainpage(acc_name):
    date = datetime.datetime.now()
    main = Tk()
    main.title("INCOME AND EXPENSE TRACKER")
    main.geometry("450x400")
    datelabel = Label(main, text="Date(DD): ", font=("Times", 15)).place(x=20,y=10)
    dd = IntVar()
    dd.set(date.day)
    dateent = Entry(main, textvariable=dd, font=("Times", 15)).place(x=110,y=12,width=27)
    monthlabel = Label(main, text="Month(MM): ", font=("Times", 15)).place(x=138,y=10)
    mm = IntVar()
    mm.set(date.month)
    monthent = Entry(main, textvariable=mm, font=("Times", 15)).place(x=247,y=12,width=27)
    yearlabel = Label(main, text="Year(YYYY): ", font=("Times", 15)).place(x=270,y=10)
    yy = IntVar()
    yy.set(date.year)
    yearent = Entry(main, textvariable=yy, font=("Times", 15)).place(x=390,y=12,width=50)
    acctype = IntVar()
    Radiobutton(text="1.Bank Account", font=("Times",15), variable=acctype, value=1).place(x=50,y=50)
    Radiobutton(text="2.Cash", font=("Times",15), variable=acctype, value=2).place(x=275,y=50)
    amountlabel = Label(main, text="Enter Amount of money", font=("Times", 15)).place(x=105,y=90)
    amountinput = StringVar()
    amount = Entry(main, font=("Times", 15), textvariable=amountinput).place(x=100,y=130)
    cate = IntVar()
    Radiobutton(text="Salary", font=("Times",15), variable=cate, value=7).place(x=50,y=160)
    Radiobutton(text="Incoming Transfer", font=("Times",15), variable=cate, value=8).place(x=50,y=190)
    Radiobutton(text="other income", font=("Times",15), variable=cate, value=9).place(x=50,y=220)
    Radiobutton(text="Food and Beverage", font=("Times",15), variable=cate, value=1).place(x=225,y=160)
    Radiobutton(text="Transportation and gas", font=("Times",15), variable=cate, value=2).place(x=225,y=190)
    Radiobutton(text="Entertainment", font=("Times",15), variable=cate, value=3).place(x=225,y=220)
    Radiobutton(text="Sport", font=("Times",15), variable=cate, value=4).place(x=225,y=250)
    Radiobutton(text="Investment", font=("Times",15), variable=cate, value=5).place(x=225,y=280)
    Radiobutton(text="other expense", font=("Times",15), variable=cate, value=6).place(x=225,y=310)
    Add = Button(main, text="Add", height=2, width=10, bg="Cyan", command=addbutton).place(x=75,y=350)
    exreport = Button(main, text="Report expenses", height=2, width=13, bg="Red").place(x=175,y=350)
    inreport = Button(main, text="Report income", height=2, width=13, bg="Green").place(x=295,y=350)
    main.mainloop()



root = Tk()
root.title("INCOME AND EXPENSE TRACKER")
root.geometry("400x300")
HeadLabel = Label(root,text="Enter your name", fg="Blue", font=("Times",30)).place(x=70,y=30)
nameinput = StringVar()
nameent = Entry(root, font=("Times",25), textvariable=nameinput).place(x=30,y=100)
loginbutton = Button(root, text="Login", height=2, width=10, bg="Cyan", command=login).place(x=80,y=180)
regbutton = Button(root, text="register", height=2, width=10, bg="Green", command=register).place(x=250,y=180) 
root.mainloop()