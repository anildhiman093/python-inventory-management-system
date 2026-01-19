from inventory import Inventory
from product import Product

inventory = Inventory()

while True:
    print("\n1. Add Product")
    print("2. View Products")
    print("3. Low Stock Alert")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        pid = input("ID: ")
        name = input("Name: ")
        price = float(input("Price: "))
        qty = int(input("Quantity: "))

        inventory.add_product(Product(pid, name, price, qty))
        print("Product added!")

    elif choice == "2":
        inventory.view_products()

    elif choice == "3":
        inventory.low_stock()

    elif choice == "4":
        break
