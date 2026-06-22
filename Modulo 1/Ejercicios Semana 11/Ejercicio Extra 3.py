class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
        pass

    def show_product_info(self):
        print(f"Nombre: {self.name}  Precio: {self.price}  Cantidad: {self.amount}")
    
    def get_price(self):
        return self.price
    def get_amount(self):
        return self.amount

class Inventory:
    def __init__(self):
        self.product = []
        pass

    def add_prduct(self, product):
        self.product.append(product)

    def show_product(self):
        for Product in self.product:
            Product.show_product_info()
    
    def show_total_inventory(self):
        total = 0
        for Product in self.product:
            current_product = Product.get_price() * Product.get_amount()
            total = total + current_product
        return total
    

product1 = Product("Mouse", 5000, 3)
product2 = Product("Teclado", 8000, 2)

inventorio = Inventory()

inventorio.add_prduct(product1)
inventorio.add_prduct(product2)

inventorio.show_product()

print(inventorio.show_total_inventory())