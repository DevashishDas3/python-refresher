import numpy

class Account:
    def __init__(self, balance, name, num):
        self.balance = balance
        self.name = name
        self.num = num

    def withdrawal(self):
        self.balance = self.balance - 1.0
        return self.balance
    
    def deposit(self):
        self.balance = self.balance + 1.0

    def display_balance(self):
        print(self.name + " has a balance of " + str(self.balance))
    

