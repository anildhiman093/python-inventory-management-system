import csv
import os

FILE_PATH = "data/inventory.csv"

def load_products():
    products = []
    if not os.path.exists(FILE_PATH):
        return products

    with open(FILE_PATH, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            products.append(row)
    return products

def save_products(products):
    os.makedirs("data", exist_ok=True)
    with open(FILE_PATH, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(products)
