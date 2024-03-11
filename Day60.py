class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}$. Current balance: {self.balance}$")
        else:
            print("Deposit amount should be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}$. Current balance: {self.balance}$")
        else:
            print("Withdrawal amount should be greater than zero and less than or equal to the balance.")

# Example usage
account = BankAccount(100)  # Creating an account with initial balance of $100
account.deposit(50)         # Deposit $50
account.withdraw(30)        # Withdraw $30
account.withdraw(200)       # Withdraw $200 (not possible due to insufficient balance)
