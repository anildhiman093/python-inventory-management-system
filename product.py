class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_list(self):
        return [self.product_id, self.name, self.price, self.quantity]
