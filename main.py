
from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

product1 = Product("Laptop", 2000, 10)
product2 = Product("Mouse", 50, 15)
product3 = Product("Keyboard", 100, 20)
manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

cart = Cart()

cart.add_product(product1)
cart.add_product(product2)

cart.display_cart()
print(f"Total value of cart: {cart.total_value()}")