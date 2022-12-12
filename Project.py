import datetime 
import numpy as np
from tkinter import *
import tkinter.messagebox
from functools import partial
import matplotlib.pyplot as plt


class Acc:
    def __init__ (self,accname):
        self.name = accname
        self.bankdatabase = np.zeros((1,13), dtype="float32")
        self.cashdatabase = np.zeros((1,13), dtype="float32")
        np.savetxt(self.name+"_bankdatabase.txt", self.bankdatabase, fmt="%f")
        np.savetxt(self.name+"_cashdatabase.txt", self.cashdatabase, fmt="%f")


    def income(self,date,a,b,x):
        date = float(date)
        if a == 1:
            self.bank_income_category(b,date,x)
        elif a == 2:
            self.cash_income_category(b,date,x)


    def expense(self,date,a,b,x):
        date = float(date)
        if a == 1:
            self.bank_expense_category(b,date,x)
        elif a == 2:
            self.cash_expense_category(b,date,x)

    def bank_income_category(self, amount, date, cate):
        if cate == 7:
            self.bankdatabase = np.append(self.bankdatabase, [[date,0,0,0,0,0,0,amount,0,0,0,0,0]], axis=0)
        if cate == 8: 
            self.bankdatabase = np.append(self.bankdatabase, [[date,0,0,0,0,0,0,0,amount,0,0,0,0]], axis=0)
        if cate == 9:
            self.bankdatabase = np.append(self.bankdatabase, [[date,0,0,0,0,0,0,0,0,amount,0,0,0]], axis=0)

    def cash_income_category(self, amount, date, cate):
        if cate == 7:
            self.cashdatabase = np.append(self.cashdatabase, [[date,0,0,0,0,0,0,amount,0,0,0,0,0]], axis=0)
        elif cate == 8: 
            self.cashdatabase = np.append(self.cashdatabase, [[date,0,0,0,0,0,0,0,amount,0,0,0,0]], axis=0)
        elif cate == 9:
            self.cashdatabase = np.append(self.cashdatabase, [[date,0,0,0,0,0,0,0,0,amount,0,0,0]], axis=0)

    def cash_expense_category(self, amount, date, cate):
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

    def bank_expense_category(self, amount, date, cate):
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


    def update_database(self):
        self.bankdatabase[0,-3] = np.sum(np.sum(self.bankdatabase, axis=0)[1:7], axis=0)
        self.bankdatabase[0,-2] = np.sum(np.sum(self.bankdatabase, axis=0)[7:10], axis=0)
        self.bankdatabase[0,-1] = self.bankdatabase[0,-2] - self.bankdatabase[0,-3]
        self.cashdatabase[0,-3] = np.sum(np.sum(self.cashdatabase, axis=0)[1:7], axis=0)
        self.cashdatabase[0,-2] = np.sum(np.sum(self.cashdatabase, axis=0)[7:10], axis=0)
        self.cashdatabase[0,-1] = self.cashdatabase[0,-2] - self.cashdatabase[0,-3]
        np.savetxt(self.name+"_bankdatabase.txt", self.bankdatabase, fmt="%f")
        np.savetxt(self.name+"_cashdatabase.txt", self.cashdatabase, fmt="%f")

        

class oldAcc(Acc):
    def __init__(self,accname):
        self.name = accname
        self.bankdatabase = np.loadtxt(self.name+"_bankdatabase.txt")
        self.cashdatabase = np.loadtxt(self.name+"_cashdatabase.txt")
        if np.ndim(self.bankdatabase) == 1:
            self.bankdatabase = self.bankdatabase.reshape(1,13)
        if np.ndim(self.cashdatabase) == 1:
            self.cashdatabase = self.cashdatabase.reshape(1,13)


def addbutton(name,date):
    acc_name = oldAcc(name)
    acc_type = acctype.get()
    acc_type = int(acc_type)
    if acc_type == 0:
        tkinter.messagebox.showinfo("Error","Please Select Account type")
    amountin = amountinput.get()
    if amountin == "":
        tkinter.messagebox.showinfo("Error", "Please Enter Amount of Money")
    else:
        amountin = float(amountin)
    x = catetype.get()
    x = str(x)
    x = int(x)
    if 1 <= x <= 6 and acc_type !=0 and amountin != "":
        acc_name.expense(date,acc_type,amountin,x)
        tkinter.messagebox.showinfo("Your account is updated", "Your expnese has been added")
    elif 7 <= x <= 9 and acc_type !=0 and amountin != "":
        acc_name.income(date,acc_type,amountin,x)
        tkinter.messagebox.showinfo("Your account is updated", "Your income has been added")
    elif x == 0:
        tkinter.messagebox.showinfo("Error","Please Select Category")
    acc_name.update_database()

def inrebutton(name):
    acc_name = oldAcc(name)
    bankre = "Your Bank Account Balance "+str(acc_name.bankdatabase[0,12])
    tkinter.messagebox.showinfo("Your Balance", bankre)
    Salary = np.sum(acc_name.bankdatabase, axis=0)[7]
    intrans = np.sum(acc_name.bankdatabase, axis=0)[8]
    others = np.sum(acc_name.bankdatabase, axis=0)[9]
    income_sum = [Salary,intrans,others]
    income_cate = ["Salary", "Incoming Transfer", "Others Income"]
    exp = [0.1,0.1,0.1]
    if Salary == 0:
        income_sum.remove(Salary)
        income_cate.remove("Salary")
        exp.remove(0.1)
    if intrans == 0:
        income_sum.remove(intrans)
        income_cate.remove("Incoming Transfer")
        exp.remove(0.1)
    if others == 0:
        income_sum.remove(others)
        income_cate.remove("Others Income")
        exp.remove(0.1)
    plt.subplot(2,1,1)
    plt.pie(income_sum, labels=income_cate, autopct="%.1f%%",shadow=True,explode=exp)
    plt.title("BankAccount Income Report", fontsize= 15)
    Salary = np.sum(acc_name.cashdatabase, axis=0)[7]
    intrans = np.sum(acc_name.cashdatabase, axis=0)[8]
    others = np.sum(acc_name.cashdatabase, axis=0)[9]
    income_sum = [Salary,intrans,others]
    income_cate = ["Salary", "Incoming Transfer", "Others Income"]
    exp = [0.1,0.1,0.1]
    if Salary == 0:
        income_sum.remove(Salary)
        income_cate.remove("Salary")
        exp.remove(0.1)
    if intrans == 0:
        income_sum.remove(intrans)
        income_cate.remove("Incoming Transfer")
        exp.remove(0.1)
    if others == 0:
        income_sum.remove(others)
        income_cate.remove("Others Income")
        exp.remove(0.1)
    plt.subplot(2,1,2)
    plt.pie(income_sum, labels=income_cate, autopct="%.1f%%",shadow=True,explode=exp)
    plt.title("CashAccount Income Report", fontsize= 15)
    plt.show()


def exrebutton(name):
    acc_name = oldAcc(name)
    food = np.sum(acc_name.bankdatabase, axis=0)[1]
    trans = np.sum(acc_name.bankdatabase, axis=0)[2]
    enter = np.sum(acc_name.bankdatabase, axis=0)[3]
    sport = np.sum(acc_name.bankdatabase, axis=0)[4]
    invest = np.sum(acc_name.bankdatabase, axis=0)[5]
    other = np.sum(acc_name.bankdatabase, axis=0)[6]
    expense_sum = [food,trans,enter,sport,invest,other]
    expense_cate = ["Food and Beverage", "Transportatino and gas", "Entertainment","Sport","Investment","Others Expenses"]
    exp = [0.1,0.1,0.1,0.1,0.1,0.1]
    if food == 0:
        expense_sum.remove(food)
        expense_cate.remove("Food and Beverage")
        exp.remove(0.1)
    if trans == 0:
        expense_sum.remove(trans)
        expense_cate.remove("Transportatino and gas")
        exp.remove(0.1)
    if enter == 0:
        expense_sum.remove(enter)
        expense_cate.remove("Entertainment")
        exp.remove(0.1)
    if sport == 0:
        expense_sum.remove(sport)
        expense_cate.remove("Sport")
        exp.remove(0.1)
    if invest == 0:
        expense_sum.remove(invest)
        expense_cate.remove("Investment")
        exp.remove(0.1)
    if other == 0:
        expense_sum.remove(other)
        expense_cate.remove("Others Expenses")
        exp.remove(0.1)
    plt.subplot(2,1,1)
    plt.pie(expense_sum, labels=expense_cate, autopct="%.1f%%",shadow=True,explode=exp)
    plt.title("BankAccount Income Report", fontsize= 15)
    food = np.sum(acc_name.cashdatabase, axis=0)[1]
    trans = np.sum(acc_name.cashdatabase, axis=0)[2]
    enter = np.sum(acc_name.cashdatabase, axis=0)[3]
    sport = np.sum(acc_name.cashdatabase, axis=0)[4]
    invest = np.sum(acc_name.cashdatabase, axis=0)[5]
    other = np.sum(acc_name.cashdatabase, axis=0)[6]
    expense_sum = [food,trans,enter,sport,invest,other]
    expense_cate = ["Food and Beverage", "Transportatino and gas", "Entertainment","Sport","Investment","Others Expenses"]
    exp = [0.1,0.1,0.1,0.1,0.1,0.1]
    if food == 0:
        expense_sum.remove(food)
        expense_cate.remove("Food and Beverage")
        exp.remove(0.1)
    if trans == 0:
        expense_sum.remove(trans)
        expense_cate.remove("Transportatino and gas")
        exp.remove(0.1)
    if enter == 0:
        expense_sum.remove(enter)
        expense_cate.remove("Entertainment")
        exp.remove(0.1)
    if sport == 0:
        expense_sum.remove(sport)
        expense_cate.remove("Sport")
        exp.remove(0.1)
    if invest == 0:
        expense_sum.remove(invest)
        expense_cate.remove("Investment")
        exp.remove(0.1)
    if other == 0:
        expense_sum.remove(other)
        expense_cate.remove("Others Expenses")
        exp.remove(0.1)
    plt.subplot(2,1,2)
    plt.pie(expense_sum, labels=expense_cate, autopct="%.1f%%",shadow=True,explode=exp)
    plt.title("CashAccount Income Report", fontsize= 15)
    plt.show()


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
            p = False
            root.destroy()
            mainpage(name)
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
            p = False
            break
    if p == True:
        accdata.append(name+"\n")
        datafile = open("acc_database.txt", "w")
        k = datafile.writelines(accdata)
        datafile.close()
        acc_name = Acc(name)
        root.destroy()
        mainpage(name)

def mainpage(acc_name):
    global acctype,amountinput,catetype
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
    datein = str(yy.get())+str(mm.get())+str(dd.get())
    acctype = IntVar()
    Radiobutton(text="1.Bank Account", font=("Times",15), variable=acctype, value=1).place(x=50,y=50)
    Radiobutton(text="2.Cash", font=("Times",15), variable=acctype, value=2).place(x=275,y=50)
    amountlabel = Label(main, text="Enter Amount of money", font=("Times", 15)).place(x=105,y=90)
    amountinput = StringVar()
    amountent = Entry(main, font=("Times", 15), textvariable=amountinput).place(x=100,y=130)
    catetype = IntVar()
    Radiobutton(text="Salary", font=("Times",15), variable=catetype, value=7).place(x=50,y=160)
    Radiobutton(text="Incoming Transfer", font=("Times",15), variable=catetype, value=8).place(x=50,y=190)
    Radiobutton(text="other income", font=("Times",15), variable=catetype, value=9).place(x=50,y=220)
    Radiobutton(text="Food and Beverage", font=("Times",15), variable=catetype, value=1).place(x=225,y=160)
    Radiobutton(text="Transportation and gas", font=("Times",15), variable=catetype, value=2).place(x=225,y=190)
    Radiobutton(text="Entertainment", font=("Times",15), variable=catetype, value=3).place(x=225,y=220)
    Radiobutton(text="Sport", font=("Times",15), variable=catetype, value=4).place(x=225,y=250)
    Radiobutton(text="Investment", font=("Times",15), variable=catetype, value=5).place(x=225,y=280)
    Radiobutton(text="other expense", font=("Times",15), variable=catetype, value=6).place(x=225,y=310)
    
    balancelabel = Label(main, text="Enter Amount of money", font=("Times", 15)).place(x=105,y=90)
    toinlabel = Label(main, text="Enter Amount of money", font=("Times", 15)).place(x=105,y=90)
    toexlabel = Label(main, text="Enter Amount of money", font=("Times", 15)).place(x=105,y=90)
    Add = Button(main, text="Add", height=2, width=10, bg="Cyan", command=partial(addbutton, acc_name,datein)).place(x=27,y=350)
    exreport = Button(main, text="Report expenses", height=2, width=13, bg="Orange", command=partial(exrebutton, acc_name)).place(x=118,y=350)
    inreport = Button(main, text="Report income", height=2, width=13, bg="Green", command=partial(inrebutton, acc_name)).place(x=230,y=350)
    delebutton = Button(main, text="Delete", height=2, width=8, bg="Red", command=partial(inrebutton, acc_name)).place(x=343,y=350)
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