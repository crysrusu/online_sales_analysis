from product import Product
class ProductManager:
   def __init__(self):
       self.products = []
   def add_product(self, product):
       self.products.append(product)
   def display_all_products(self):
       for product in self.products:
           product.display_product_info()
   def total_inventory_value(self):
       total = 0
       for product in self.products:
           total += product.price * product.quantity
       return total
   def remove_product_by_name(self, product_name);
	self.products= [p for p in self.products if p.name !=product_name]