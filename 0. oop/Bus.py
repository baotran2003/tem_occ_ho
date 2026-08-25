from typing import List

class Bus:
    def __init__(self):
        self.capacity: int = 15
        self.passenger: List[str] = []

    def reserve(self, name: str):
        if len(self.passenger) < self.capacity:
            if name not in self.passenger:
                self.passenger.append(name)
                print("Reservation successfully !")
            else:
                print("Passenger already has s reservation !")

        else:
            print("Seats not available")


    def cancel_reservation(self, name: str):
        if name in self.passenger:
            self.passenger.remove(name)
            print("Cancel reservation successfully !")
        else:
            print("Not found passenger !")


    def show_seats(self):
        available: int = self.capacity -  len(self.passenger)
        print("\n----------Bus Status----------")
        print("Total Seats: ", self.capacity)
        print("Available Seats: ", available)

        if self.passenger:
            print("Number of passenger:")
            i: int = 1
            for passenger in self.passenger:
                print(i, "-", passenger)
                i+= 1
        else:
            print("Not reservation yet !")

if __name__ == "__main__":
    bus: Bus = Bus()
    while True:
        print("\n----------Bus Reservation System----------")
        print("1. Reserve Seats\n2. Cancel Reservation\n3. Show Status Bus\n4. Exit")

        try:
            choice: int = int(input("Enter your choice: "))
            if choice == 1:
                name: str = input("Enter Passenger Name: ")
                bus.reserve(name)

            elif choice == 2:
                name: str = input("Enter Passenger Name: ")
                bus.cancel_reservation(name)
            elif choice == 3:
                bus.show_seats()
            elif choice == 4:
                print("Thank you !")
                break
            else:
                print("Invalid choice")

        except ValueError:
            print("Invalid input !")
            continue

