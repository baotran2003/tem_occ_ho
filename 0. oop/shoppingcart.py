# Simple Shopping Cart System in python OOPs
# 1. Add item   2. Remove item  3. Show Cart    4. Total bill   5. exit

class Product:
    def __init__(self, product_id: int, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_product(self):
        print(f"{self.product_id}. {self.name} - ${self.price}")

class ShoppingCart:
    def __init__(self):
        self.cart: dict[int, dict] = {}

    def add_item(self, product: Product, quantity: int) -> None:
        product.display_product()
        print(f"Quantity: {quantity}")

        if product.product_id in self.cart:
            self.cart[product.product_id]["quantity"] += quantity
        else:
            self.cart[product.product_id] = {
                "product": product,
                "quantity": quantity
            }

        print("Product added successfully!")


    def remove_item(self, product_id: int) -> None:
        if product_id in self.cart:
            del self.cart[product_id]
            print("Product removed successfully !")
        else:
            print("Product not found !")

    def display_cart(self) -> float:
        total = 0

        for item in self.cart.values():
            product = item["product"]
            quantity = item["quantity"]
            subtotal = product.price * quantity
            total += subtotal

            print(f"{product.name} - ${product.price} x {quantity} = ${subtotal}")

        print("----------")
        print(f"Total bill: ${total}")

        return total

    def show_cart(self) -> None:
        if not self.cart:
            print("Cart is empty !")
            return

        print("\nShopping Cart")
        self.display_cart()

    def checkout(self) -> None:
        if not self.cart:
            print("Shopping cart is empty !")
            return

        print("\nInvoice")
        total = self.display_cart()

        print("Checkout successful!")
        print(f"Total payment: ${total}")

        self.cart.clear()

if __name__ == "__main__":
    products = {
        1: Product(1, "Laptop", 1000),
        2: Product(2, "Mouse", 20),
        3: Product(3, "Keyboard", 50)
    }
    cart: ShoppingCart = ShoppingCart()

    while True:
        print("\n----------Shopping Cart System----------")
        print("1. Show Products")
        print("2. Add Product To Cart")
        print("3. Remove Product")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        try:
            choice: int = int(input("Enter your choice: "))

            if choice == 1:
                print("\nAvailable Products")
                for product in products.values():
                    product.display_product()
            elif choice == 2:
                product_id: int = int(input("Enter product id: "))
                quantity: int = int(input("Enter quantity: "))
                if product_id in products:
                    cart.add_item(products[product_id], quantity)
                else:
                    print("Product id not found in products !")

            elif choice == 3:
                product_id: int = int(input("Enter product id: "))
                cart.remove_item(product_id)
            elif choice == 4:
                cart.show_cart()
            elif choice == 5:
                cart.checkout()
            elif choice == 6:
                print("GoodBye !!!!")
                break
            else:
                print("Invalid Choice !")
        except ValueError:
            print("Invalid input!")
            continue