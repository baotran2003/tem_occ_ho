class Hotel:
    def __init__(self):
        self.rooms: dict[int, None] = {
            101: None,
            102: None,
            103: None
        }

    def show_room(self):
        print("\nRoom Status")
        for room, guest in self.rooms.items():
            if guest is None:
                print(room, "-Available")
            else:
                print(room, "-Booked by", guest)

    def book_room(self, room, guest_name):
        if room in self.rooms and self.rooms[room] is None:
            self.rooms[room] = guest_name
            print("Room booked successfully!")
        else:
            print(f"Room {room} not available")

    def cancel_booking(self, room):
        if room in self.rooms and self.rooms[room] is not None:
            self.rooms[room] = None
            print("Booking cancel successfully!")
        else:
            print("Room is already available!")
if __name__ == "__main__":
    hotel: Hotel = Hotel()

    while True:
        print("\n__________Hotel System Management__________")
        print("1. Show Rooms\n2. Book Rooms\n3. Cancel Booking\n4. Exist")

        choice: int = int(input("Enter your choice: "))

        if choice == 1:
            hotel.show_room()
        elif choice == 2:
            room_number: int = int(input("Enter room number: "))
            guest_name = input("Enter guest name: ")
            hotel.book_room(room_number, guest_name)
        elif choice == 3:
            room_number: int = int(input("Enter room number: "))
            hotel.cancel_booking(room_number)
        elif choice == 4:
            print("Thank your for using Hotel Management System")
            break
        else:
            print("Invalid Choice !")
