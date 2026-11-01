from abc import ABC, abstractmethod
from datetime import datetime


# Abstract Class
class Account(ABC):

    def __init__(self, name, account_number, balance=0):
        if not name.strip():
            raise ValueError("Name cannot be empty")

        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.name = name
        self.account_number = account_number
        self.__balance = float(balance)
        self.transactions = []

        if balance > 0:
            self.add_transaction("Opening Deposit", balance)

    # Encapsulation
    @property
    def balance(self):
        return self.__balance

    def add_transaction(self, transaction_type, amount):
        date = datetime.now()
        self.transactions.append(
            f"{date} | {transaction_type} | Rs.{amount}"
        )

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Enter a valid amount")

        self.__balance += amount
        self.add_transaction("Deposit", amount)
        print("Money deposited successfully!")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Enter a valid amount")

        if amount > self.__balance:
            raise ValueError("Insufficient balance")

        self.__balance -= amount
        self.add_transaction("Withdrawal", amount)
        print("Money withdrawn successfully!")

    @abstractmethod
    def account_type(self):
        pass

    def display_details(self):
        print("\nAccount Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Account Type:", self.account_type())
        print("Balance: Rs.", self.balance)

    def transaction_history(self):
        print("\nTransaction History")

        if not self.transactions:
            print("No transactions found")

        for transaction in self.transactions:
            print(transaction)


# Inheritance
class SavingsAccount(Account):

    def account_type(self):
        return "Savings Account"


class CurrentAccount(Account):

    def account_type(self):
        return "Current Account"


# Bank Class
class Bank:

    def __init__(self):
        self.accounts = {}

    def create_account(self):
        try:
            name = input("Enter account holder name: ")
            number = input("Enter account number: ")

            if number in self.accounts:
                raise ValueError("Account already exists")

            print("1. Savings Account")
            print("2. Current Account")

            choice = input("Choose account type: ")

            if choice == "1":
                account = SavingsAccount(
                    name, number
                )

            elif choice == "2":
                account = CurrentAccount(
                    name, number
                )

            else:
                raise ValueError("Invalid account type")

            self.accounts[number] = account

            print("Account created successfully!")

        except ValueError as e:
            print("Error:", e)

    def find_account(self):
        number = input("Enter account number: ")

        account = self.accounts.get(number)

        if account is None:
            print("Account not found")

        return account

    def deposit_money(self):
        account = self.find_account()

        if account:
            try:
                amount = float(input("Enter amount: "))
                account.deposit(amount)

            except ValueError as e:
                print("Error:", e)

    def withdraw_money(self):
        account = self.find_account()

        if account:
            try:
                amount = float(input("Enter amount: "))
                account.withdraw(amount)

            except ValueError as e:
                print("Error:", e)

    def check_balance(self):
        account = self.find_account()

        if account:
            print("Balance: Rs.", account.balance)

    def show_details(self):
        account = self.find_account()

        if account:
            account.display_details()

    def show_history(self):
        account = self.find_account()

        if account:
            account.transaction_history()

    def menu(self):

        while True:

            print("\n===== PYTHON BANKING SYSTEM =====")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Account Details")
            print("6. Transaction History")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_account()

            elif choice == "2":
                self.deposit_money()

            elif choice == "3":
                self.withdraw_money()

            elif choice == "4":
                self.check_balance()

            elif choice == "5":
                self.show_details()

            elif choice == "6":
                self.show_history()

            elif choice == "7":
                print("Thank you!")
                break

            else:
                print("Invalid choice")


# Main Program
if __name__ == "__main__":

    bank = Bank()
    bank.menu()