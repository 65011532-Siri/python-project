import datetime 
import numpy as np


class Acc:
    def __init__ (self,accname, bankacc = 0.0, cashacc = 0.0):
        self.name = accname
        self.bank_balance = bankacc
        self.cash_balance = cashacc
        self.dt = datetime.datetime.now()
        self.firstday = str(self.dt.year)+str(self.dt.month)+str(self.dt.day)
        self.bankdatabase = np.empty((1,3), dtype="float32")
        self.cashdatabase = np.empty((1,3), dtype="float32")
        self.bankdatabase [0,0] = float(self.firstday) #[0,0] is date
        self.cashdatabase [0,0] = float(self.firstday) #[0,0] is date
        self.bankdatabase [0,1], self.bankdatabase[0,2] = 0,0 #[0,1] is bank_balance
        self.cashdatabase [0,1], self.cashdatabase[0,2]=  0,0 #[0,1] is cash_balance
        np.savetxt(self.name+"_bankdatabase.txt", self.bankdatabase, fmt="%f")
        np.savetxt(self.name+"_cashdatabase.txt", self.cashdatabase, fmt="%f")


    def report(self):
        print("1.Bank Account or 2.Cash Account")
        a = int(input())
        if a == 1:
            print("Bank Account:", self.bank_balance)
        elif a == 2: 
            print("Cash Account: ", self.cash_balance)

    def income(self):
        date = dateinput()
        print("1.Bank Account or 2.Cash Account")
        a = int(input())
        b = float(input("Amount of money: "))
        if a == 1:
            self.bank_balance += b
            self.bankdatabase = np.append(self.bankdatabase, [[date,0,b]], axis=0)
            return self.bank_balance

        elif a == 2:
            self.cash_balance += b
            self.cashdatabase = np.append(self.cashdatabase, [[date,0,b]], axis=0)
            return self.cash_balance


    def expense(self):
        print("1.Bank Account or 2.Cash Account")
        a = int(input())
        b = float(input("Amount of money: "))
        if a == 1:
            self.bank_balance -= b
            return self.bank_balance
        elif a == 2:
            self.cash_balance -= b
            return self.cash_balance

    def update_bankdatebase(self):
        self.bankdatabase[0,1] = np.sum(self.bankdatabase, axis=0)[2]
        self.cashdatabase[0,1] = np.sum(self.cashdatabase, axis=0)[2]
        np.savetxt(self.name+"_bankdatabase.txt", self.bankdatabase, fmt="%f")
        np.savetxt(self.name+"_cashdatabase.txt", self.cashdatabase, fmt="%f")


def dateinput(x = datetime.datetime.now()):
    print("Select date: 1.Today 2.customs day")
    i = int(input())
    if i == 2:
        print("Enter month: ")
        mm = input()
        print("Enter date: ")
        dd = input()
        print("Enter year(20xx): ")
        yy = input()
        x = datetime.datetime(yy, mm, dd)
    x = str(x.year)+str(x.month)+str(x.day)
    return float(x)

class oldAcc(Acc):
    def __init__(self,accname):
        self.name = accname
        self.bankdatabase = np.loadtxt(self.name+"_bankdatabase.txt")
        self.cashdatabase = np.loadtxt(self.name+"_cashdatabase.txt")
        if np.ndim(self.bankdatabase) == 1:
            self.bankdatabase = self.bankdatabase.reshape(1,3)
        if np.ndim(self.cashdatabase) == 1:
            self.cashdatabase = self.cashdatabase.reshape(1,3)    
        self.bank_balance = self.bankdatabase [0,1]
        self.cash_balance = self.cashdatabase [0,1]





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
    print(accdata)

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
    