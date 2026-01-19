from product import Product
from storage import load_products, save_products

class Inventory:
    def __init__(self):
        self.products = load_products()

    def add_product(self, product: Product):
        self.products.append(product.to_list())
        save_products(self.products)

    def view_products(self):
        for p in self.products:
            print(p)

    def low_stock(self, limit=5):
        for p in self.products:
            if int(p[3]) <= limit:
                print("LOW STOCK:", p)
