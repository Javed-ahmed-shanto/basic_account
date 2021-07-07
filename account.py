class Account():
    def __init__(self,owner,balance):
        self.name = owner
        self.balance = balance
    def deposit(self, deposit_amount):
        self.balance = deposit_amount + self.balance
        print(f"you recently added {deposit_amount}$")
        print(f"your Current Balance is {self.balance}$")
    def withdraw(self, withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance = self.balance - withdraw_amount
            print(f"you have withdrawn {withdraw_amount}$")
            print(f'so your new balance is {self.balance}$')
            
            
acc = Account('Javed Ahmed Shanto', 100000)
acc.deposit(999)
acc.balance
acc.deposit(1)
acc.withdraw(1)
