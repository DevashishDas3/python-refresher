import numpy

class Account:
    def __init__(self, name, account_num, balance = 0.0):
        self.balance = balance
        self.name = name
        self.num = account_num

    def withdrawal(self, amount):
        if amount >= self.balance:
            self.balance-=amount
            return self.balance
        else:
            raise ValueError(f'Cannot withdraw {amount} from a balance of {self.balance}')
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Requested deposit is negative!")

    def display_balance(self):
        print(f'{self.name} has a balance of {str(self.balance)}')
    

