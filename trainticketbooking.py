class Train:
    def __init__(self, train_no, train_name, seats):
        self.train_no = train_no
        self.train_name = train_name
        self.available_seats = seats

trains = {
    101: Train(101, "Express", 5),
    102: Train(102, "Super Fast", 3),
    103: Train(103, "Intercity", 4)
}

reservations = {}
pnr_counter = 1000


def show_trains():
    print("\nAvailable Trains")
    print("-" * 40)
    for train in trains.values():
        print(
            f"Train No: {train.train_no}, "
            f"Train Name: {train.train_name}, "
            f"Available Seats: {train.available_seats}"
        )


def book_ticket():
    global pnr_counter

    train_no = int(input("Enter Train Number: "))
    name = input("Enter Passenger Name: ")

    if train_no not in trains:
        print("Invalid Train Number!")
        return

    train = trains[train_no]

    if train.available_seats > 0:
        train.available_seats -= 1
        pnr_counter += 1

        reservations[pnr_counter] = {
            "name": name,
            "train_no": train_no,
            "train_name": train.train_name
        }

        print("\nTicket Booked Successfully!")
        print("PNR Number:", pnr_counter)
    else:
        print("No seats available!")


def cancel_ticket():
    pnr = int(input("Enter PNR Number to Cancel: "))

    if pnr in reservations:
        train_no = reservations[pnr]["train_no"]

        trains[train_no].available_seats += 1

        del reservations[pnr]

        print("Ticket Cancelled Successfully!")
    else:
        print("Invalid PNR Number!")


def view_reservations():
    if not reservations:
        print("No Reservations Found!")
        return

    print("\nReservation Details")
    print("-" * 40)

    for pnr, details in reservations.items():
        print(f"PNR: {pnr}")
        print(f"Passenger: {details['name']}")
        print(f"Train No: {details['train_no']}")
        print(f"Train Name: {details['train_name']}")
        print("-" * 40)


while True:
    print("\n===== Railway Reservation System =====")
    print("1. Show Trains")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. View Reservations")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        show_trains()
    elif choice == "2":
        book_ticket()
    elif choice == "3":
        cancel_ticket()
    elif choice == "4":
        view_reservations()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")