class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
    def withdraw(self, amount):
        pass
    def check_balance(self):
        print("Account Holder:", self.name)
        print("Current Balance:", self.balance)
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Savings Withdrawal:", amount)
        else:
            print("Insufficient Balance in Savings Account")
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        limit = self.balance + 5000
        if amount <= limit:
            self.balance -= amount
            print("Current Account Withdrawal:", amount)
        else:
            print("Overdraft Limit Exceeded")
class ATM:

    def __init__(self, account):
        self.account = account

    def atm_menu(self):

        while True:
            print("\n----- ATM MENU -----")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                amount = float(input("Enter deposit amount: "))
                self.account.deposit(amount)

            elif choice == 2:
                amount = float(input("Enter withdrawal amount: "))
                self.account.withdraw(amount)

            elif choice == 3:
                self.account.check_balance()

            elif choice == 4:
                print("Thank You!")
                break

            else:
                print("Invalid Choice")


user1 = SavingsAccount("Naveena", 50000)
atm = ATM(user1)
atm.atm_menu()