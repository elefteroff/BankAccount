class BankAccount:

    all_accounts = []

    def __init__(self, acct, balance = 0, int_rate = 0.0025):
        self.balance = balance
        self.acct = acct
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)

    def deposit(self, amount, acct):
        self.balance += amount
        self.acct = acct
        return self
        
    def withdraw(self, amount, acct):
        self.balance -= amount
        self.acct = acct
        return self

    def display_account_info(self):
        print(f"Bank Account: {self.acct}, Account Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance + (self.int_rate * self.balance)
        return self

    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()   

Acct1 = BankAccount("Checking")
Acct2 = BankAccount("Savings")

Acct1.deposit(500, "Checking").deposit(500, "Checking").deposit(500, "Checking").withdraw(300, "Checking").display_account_info().yield_interest().display_account_info()

Acct2.deposit(1000, "Savings").deposit(2000, "Savings").withdraw(500, "Savings").withdraw(300, "Savings").withdraw(200, "Savings").withdraw(400, "Savings").display_account_info().yield_interest().display_account_info()

BankAccount.all_balances()