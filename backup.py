import datetime 
import numpy as np


class Acc:
    def __init__ (self,accname, bankacc = 0.0, cashacc = 0.0):
        self.name = accname
        self.bank_balance = bankacc
        self.cash_balance = cashacc
        self.dt = datetime.datetime.now()
        self.firstday = str(self.dt.year)+str(self.dt.month)+str(self.dt.day)
        self.database = np.empty((0,3), dtype=str)


    def report(self):
        print("1.Bank Account or 2.Cash Account")
        a = int(input())
        if a == 1:
            print("Bank Account:", self.bank_balance)
        elif a == 2: 
            print("Cash Account: ", self.cash_balance)

    def income(self):
        date = today()
        print("1.Bank Account or 2.Cash Account")
        a = int(input())
        b = float(input("Amount of money: "))
        if a == 1:
            self.bank_balance += b
            self.database = np.append(self.database, np.array[])
            return self.bank_balance

        elif a == 2:
            self.cash_balance += b
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


def today(x = datetime.datetime.now()):
    print("Select date: 1.Today 2.customs day")
    i = int(input())
    if i == 2:
        print("Enter month: ")
        mm = input()
        print("Enter date: ")
        dd = input()
        print("Enter year: ")
        yy = input()
        x = datetime.datetime(yy, mm, dd)
    return x


name = input("Enter your name: ")
acc_name = Acc(name)

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