class Account:
    def __init__(self, account_no, name, balance=0):
        self.account_no = account_no
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append({"type": "deposit", "amount": amount})
        print(f"{self.name} deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            self.transactions.append({"type": "failed_withdrawal", "amount": amount})
            print(f"{self.name} has insufficient funds for ${amount}. Current balance: ${self.balance}")
            return False
        self.balance -= amount
        self.transactions.append({"type": "withdrawal", "amount": amount})
        print(f"{self.name} withdrew ${amount}. New balance: ${self.balance}")
        return True

    def get_balance(self):
        return self.balance

    def show_transactions(self):
        print(f"Transaction history for {self.name}:")
        for t in self.transactions:
            print(f"  - {t['type'].capitalize()}: ${t['amount']}")


class BankSystem:
    def __init__(self):
        self.accounts = {}  # HashMap: account_no -> Account

    # Add a new account
    def add_account(self, account_no, name, balance=0):
        if account_no in self.accounts:
            print(f"Account {account_no} already exists.")
            return False
        self.accounts[account_no] = Account(account_no, name, balance)
        print(f"Account {account_no} created for {name} with balance ${balance}")
        return True

    # Get account by account_no
    def get_account(self, account_no):
        return self.accounts.get(account_no, None)

    # Perform deposit
    def deposit(self, account_no, amount):
        acc = self.get_account(account_no)
        if acc:
            acc.deposit(amount)
        else:
            print(f"Account {account_no} not found.")

    # Perform withdrawal
    def withdraw(self, account_no, amount):
        acc = self.get_account(account_no)
        if acc:
            acc.withdraw(amount)
        else:
            print(f"Account {account_no} not found.")

    # Show all accounts
    def show_all_accounts(self):
        for acc_no, acc in self.accounts.items():
            print(f"{acc_no} | {acc.name} | Balance: ${acc.balance}")


bank = BankSystem()
bank.add_account("ACC1001", "Alice", 1500)
bank.add_account("ACC1002", "Bob", 2300)
bank.add_account("ACC1003", "Charlie", 500)

print("\n=== Deposits and Withdrawals ===")
bank.deposit("ACC1001", 300)
bank.withdraw("ACC1003", 200)
bank.withdraw("ACC1003", 1000)  # Edge case: insufficient funds
bank.withdraw("ACC9999", 50)    # Edge case: non-existent account

print("\n=== Final Account Balances ===")
bank.show_all_accounts()

print("\n=== Transaction History ===")
for acc in bank.accounts.values():
    acc.show_transactions()
