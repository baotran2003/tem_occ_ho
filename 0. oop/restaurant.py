from typing import List

class Restaurant:
    def __init__(self):
        self.menu: dict[str, int] = {
            "Burger": 5000,
            "Coffee": 100000,
            "Pizza": 34500
        }
        self.orders: List[int] = []

    def show_menu(self):
        print("__________MENU__________")
        for item, price in self.menu.items():
            print(f"{item} -- {price} VND")

    def order(self, item):
        if item in self.menu:
            self.orders.append(item)
            print(item, "added to the cart.")
        else:
            print("item is not available.")

    def bill(self):
        total_bill: int = 0
        print("\n_____Your Order_____")
        for item in self.orders:
            print(item, "--", self.menu[item], "VND")
            total_bill += self.menu[item]

        print("----------")
        print("Total Bill: ", total_bill, "VND")

if __name__ == "__main__":
    r: Restaurant = Restaurant()
    while True:
        r.show_menu()

        food: str = input("Enter food name: ")
        r.order(food)

        more: str = input("Order more (yes/no): ")
        if more.lower() != "yes":
            break
    r.bill()