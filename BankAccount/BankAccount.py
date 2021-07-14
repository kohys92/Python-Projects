class BankAccount:

    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account Owner: {self.owner} \nAccount balance: ${self.balance}"

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Deposit Accepted")

    def withdraw(self,amount):
        if self.balance > amount:
            self.balance = self.balance - amount
            print("Withdrawal Accepted")

        else:
            print("Funds unavailable!")

acct1 = BankAccount("Jose",100)
acct2 = BankAccount("Owen",50)

print(acct1)
print(acct2)

acct1.deposit(50)
acct2.withdraw(20)

print(acct1)
print(acct2)

acct2.withdraw(100)
print(acct2)
