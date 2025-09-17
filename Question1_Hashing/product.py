# class Product stores baby product info of the retail store
class Product:
    def __init__(self, product_id, name, category, brand, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.brand = brand
        self.price = price
        self.stock_quantity = stock_quantity

    # function to print the information
    def __str__(self):
        return (f"ID: {self.product_id}, "
                f"Name: {self.name}, "
                f"Category: {self.category}, "
                f"Brand: {self.brand}, "
                f"Price: RM{self.price:.2f}, "
                f"Stock: {self.stock_quantity}")
