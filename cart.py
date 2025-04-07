
class Cart:
   def __init__(self):
       self.cart_items = []
   def add_product(self, product):
       self.cart_items.append(product)
   def total_value(self):
       return sum([product.price * product.quantity for product in self.cart_items])
   def display_cart(self):
       for product in self.cart_items:
           print(f"Product: {product.name}, Price: {product.price}, Quantity: {product.quantity}")