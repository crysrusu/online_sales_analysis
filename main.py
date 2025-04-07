from product import Product
from product_manager import ProductManager

manager = ProductManager()

manager.add_product(Product("Laptop", 3500, 5))
manager.add_product(Product("Mouse", 150, 20))
manager.add_product(Product("Monitor", 1200, 10))

print("Produse în stoc:")
manager.display_all_products()

print(f"\nValoarea totală a stocului: {manager.total_inventory_value()} RON")