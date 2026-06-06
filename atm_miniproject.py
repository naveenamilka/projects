balance=0
pin=1234
transactions=[]
def credit():
    global balance
    global transactions
    amount=float(input("enter amount to credit:"))
    balance+=amount
    transactions.append(f"credited:{amount}")
    print(f"{amount}credited to your account")
def debit():
    global balance
    amount=float(input("enter amount to debit:"))
    if amount>balance:
        print("insufficient balance.")
    else:
        balance-=amount
        transactions.append(f"debited:{amount}")
        print(f"{amount} debited from your account")
        print("transaction completed")
def bal():
    global balance
    print(f"your current balance is {balance}")
def pinchange():
    global pin
    old_pin=int(input("enter old pin"))
    if old_pin==pin:
        new_pin=input("enter new_pin:")
        if len(new_pin)==4 and new_pin.isdigit():
            pin=int(new_pin)
            print("pin changed sucessfully")
        else:
            print("pin must contain 4 digits")
    else:
        print("incorrect old_pin")

def ministatement():
    print("\n--- MINI STATEMENT ---")

    if len(transactions) == 0:
        print("No transactions available")

    else:
        for t in transactions:
            print(t)
def exit():
    print(f"transaction completed")
while True:
    print("\n ATM MENU")
    print("1.Credit")
    print("2.Debit")
    print("3.Balance")
    print("4.pinchange")
    print("5.ministatement")
    print("6.exit")
    choice=int(input("enter choice(1-6)"))
    if choice==1:
        credit()
    elif choice==2:
        debit()
    elif choice==3:
        bal()
    elif choice==4:
        pinchange()
    elif choice==5:
        ministatement()
    elif choice==6:
        exit()
        break