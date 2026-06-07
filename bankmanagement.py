class BankAccount:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def show_details(self):
        print("\n----- Account Details -----")
        print("Account Number:", self.acc_no)
        print("Account Holder:", self.name)
        print("Balance: ₹", self.balance)


accounts = {}


def create_account():
    acc_no = int(input("Enter Account Number: "))

    if acc_no in accounts:
        print("Account already exists!")
        return

    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Deposit: "))

    accounts[acc_no] = BankAccount(acc_no, name, balance)
    print("Account Created Successfully!")


def deposit_money():
    acc_no = int(input("Enter Account Number: "))

    if acc_no in accounts:
        amount = float(input("Enter Amount to Deposit: "))
        accounts[acc_no].deposit(amount)
    else:
        print("Account not found!")


def withdraw_money():
    acc_no = int(input("Enter Account Number: "))

    if acc_no in accounts:
        amount = float(input("Enter Amount to Withdraw: "))
        accounts[acc_no].withdraw(amount)
    else:
        print("Account not found!")


def check_balance():
    acc_no = int(input("Enter Account Number: "))

    if acc_no in accounts:
        print("Current Balance: ₹", accounts[acc_no].balance)
    else:
        print("Account not found!")


def view_account():
    acc_no = int(input("Enter Account Number: "))

    if acc_no in accounts:
        accounts[acc_no].show_details()
    else:
        print("Account not found!")


while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. View Account Details")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit_money()
    elif choice == "3":
        withdraw_money()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        view_account()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")