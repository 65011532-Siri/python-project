import datetime 
import numpy as np


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


p = True
name = input("Enter your name: ")
file = open("acc_database.txt", "r")
b = len(file.readlines())
file = open("acc_database.txt", "r")
accdata = file.readlines()
for i in range(b):
    file = open("acc_database.txt", "r")
    a = file.readlines()[i]
    a = a.strip("\n")
    if name == a:
        acc_name = oldAcc(name)
        p = False
        break

if p == True:
    acc_name = Acc(name)
    accdata.append(name+"\n")
    datafile = open("acc_database.txt", "w")
    k = datafile.writelines(accdata)
    datafile.close()

while True:
    print("Run a command")
    c = input()
    if c=='q':
        print("Done")
        break
    elif c=="report":
        acc_name.report()
    elif c=="income":
        acc_name.income()
    elif c=="expense":
        acc_name.expense()
    else:
        print("Invalid command")
    acc_name.update_bankdatebase()
    