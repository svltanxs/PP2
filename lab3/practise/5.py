class Account:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited{amount} , new balance: {self.balance}")
    def withdraw(self, amount):
        if (amount > self.balance):
            print(f"withdraw of {amount} denied,You have a only {self.balance}")
        else:
            self.balance -= amount
            print(f"You take {amount} money, New balance: {self.balance}")
acc = Account("Sultanbek" , 100)
acc.deposit(50)
acc.deposit(20)

acc.withdraw(100)
acc.withdraw(1000)

print(f"Final balance {acc.balance}")