customername = input("Enter customer name: ")

lists = '''
Rice       Rs1000/bag
Teapowder  Rs50/packet
Oil        Rs100/packet
Flour      Rs100/kg
Bottles    Rs60/2
Soap       Rs30
'''

totalprice = 0
bill_items = []

items = {
    "rice": 1000,
    "teapowder": 50,
    "oil": 100,
    "flour": 100,
    "bottles": 60,
    "soap": 30
}

while True:
    option = input("Enter 1 for shopping or 2 to exit: ")

    if option == "2":
        print("Thank you for shopping")
        break

    elif option == "1":
        print(lists)

        while True:
            process = input("To Buy Enter 1 or Enter 2 for billing: ")

            if process == "2":
                break

            elif process == "1":

                item = input("Choose your item: ").lower()

                if item in items:

                    while True:
                        quantity_ip = input("Enter Quantity: ")

                        if quantity_ip.isdigit():
                            quantity = int(quantity_ip)
                            break
                        else:
                            print("Please enter a valid quantity")

                    price = quantity * items[item]
                    totalprice += price

                    bill_items.append((item, quantity, items[item], price))

                    print(f"{item} added successfully!")

                else:
                    print("Selected item is not available.")

        # Billing Section
        if totalprice > 0:
            tax = (totalprice * 18) / 100
            finalprice = totalprice + tax

            print("\n", 25 * "=", "NR Supermarket", 25 * "=")
            print(" " * 30, "")
            print(f"Customer Name: {customername}")
            print("-" * 75)
            print("S.No\tItem\t\tQty\tPrice")
            for i in range(len(bill_items)):
                item, qty, unit_price, total = bill_items[i]
                print(f"{i+1}\t{item}\t\t{qty}\tRs {total}")

            print("-" * 75)
            print(f"Total Amount:\t\t\tRs {totalprice}")
            print(f"Tax Amount (18%):\t\tRs {tax}")
            print("-" * 75)
            print(f"Final Amount:\t\t\tRs {finalprice}")
            print("-" * 75)
            print("\tThank You & Visit Again")
            print("-" * 75)