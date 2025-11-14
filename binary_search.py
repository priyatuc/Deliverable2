# --- Account Class ---
class Account:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"{self.name} has insufficient funds to withdraw ${amount}. Current balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"{self.name} withdrew ${amount}. New balance: ${self.balance}")

    def __str__(self):
        return f"{self.account_no} | {self.name} | ${self.balance}"


# --- BST Node ---
class Node:
    def __init__(self, account):
        self.account = account
        self.left = None
        self.right = None


# --- BST Class ---
class BST:
    def __init__(self):
        self.root = None

    # Insert account
    def insert(self, account):
        if self.root is None:
            self.root = Node(account)
        else:
            self._insert(self.root, account)

    def _insert(self, current, account):
        if account.account_no < current.account.account_no:
            if current.left:
                self._insert(current.left, account)
            else:
                current.left = Node(account)
        elif account.account_no > current.account.account_no:
            if current.right:
                self._insert(current.right, account)
            else:
                current.right = Node(account)
        else:
            # Duplicate account number: update balance
            current.account.balance = account.balance

    # Search account
    def search(self, account_no):
        return self._search(self.root, account_no)

    def _search(self, current, account_no):
        if current is None:
            return None
        if account_no == current.account.account_no:
            return current.account
        elif account_no < current.account.account_no:
            return self._search(current.left, account_no)
        else:
            return self._search(current.right, account_no)

    # In-order traversal
    def inorder_traversal(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, current, result):
        if current:
            self._inorder(current.left, result)
            result.append(current.account)
            self._inorder(current.right, result)


def demo_banking_bst():
    bank_bst = BST()

    # Create accounts
    bank_bst.insert(Account("ACC1001", "Alice", 1500.00))
    bank_bst.insert(Account("ACC1005", "Bob", 2300.00))
    bank_bst.insert(Account("ACC1003", "Charlie", 500.00))

    print("=== All Accounts (Sorted) ===")
    for acc in bank_bst.inorder_traversal():
        print(acc)

    # Deposit money
    account = bank_bst.search("ACC1003")
    if account:
        account.deposit(200)

    # Withdraw money
    account = bank_bst.search("ACC1005")
    if account:
        account.withdraw(300)

    # Attempt to withdraw more than balance
    account = bank_bst.search("ACC1003")
    if account:
        account.withdraw(1000)

    # Search non-existent account
    account = bank_bst.search("ACC9999")
    if not account:
        print("Account ACC9999 not found.")

    print("\n=== Final Account Balances ===")
    for acc in bank_bst.inorder_traversal():
        print(acc)

# Run demo
demo_banking_bst()
