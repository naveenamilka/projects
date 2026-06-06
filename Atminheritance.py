class BankAccount():
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposited amount:-",amount)
        print("current balance:-",self.balance)
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("withdrawl amount",amount)
            print("current balance",self.balance)
        else:
            print("insufficent balance")
    def check_balance(self):
        print("Account Holder",self.name)
        print("Balance",self.balance)
class ATM(BankAccount):
    def ATM_MENU(self):
        while True:
            print("\n -----ATM MENU-----")
            print("1.Deposit")
            print("2.withdraw")
            print("3.checkbalance")
            print("4.exit")

            choice=int(input("enter your choice"))
            if choice==1:
                amount=float(input("enter deposit amount:"))
                self.deposit(amount)
            elif choice==2:
                amount=float(input("enter withdraw amount:"))
                self.withdraw(amount)
            elif choice==3:
                self.check_balance()
            elif choice==4:
                print("Thank You!")
                break
            else:
                print("invalid choice")

user=ATM("Naveena",50000)
user.ATM_MENU()
