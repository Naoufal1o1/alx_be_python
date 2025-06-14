# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize a bank account with an optional initial balance (default is 0)."""
        self.__account_balance = initial_balance  # Private attribute for encapsulation

    def deposit(self, amount):
        """Add the given amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Subtract the given amount from the account balance if sufficient funds exist.
        Returns True if successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
