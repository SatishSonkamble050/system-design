import uuid

class User:
    def __init__(self, name, role):
        self.id = str(uuid.uuid4())
        self.role = role
        self.name = name

class Products:
    def __init__(self,id, p_name, price, quantity):
        self.id = id
        self.p_name = p_name
        self.price = price
        self.quantity = quantity

    
    def add_quantity(self, count):
        self.quantity += count
    
    def remove_quantity(self, count):
        self.quantity -= count

class Cart:
    def __init__(self, id):
        self.id = id
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product):
        self.items = [s for s in self.add_items if s.id != product.id]
    
class order:
    def __init__(self, id, items):
        self.id = id
        self.items = items


class ECommer:
    def __init__(self):
        self.products = []
        self.orders = []
        self.cart = []

    def create_user():
        pass
    def create_product(self, product):
        self.products.append(product)

    def add_item_in_cart(self, item):
        self.cart.append(item)

    def remove_item_from_cart(self, item):
        self.cart = [s for s in self.cart if s.id != item.id ]

    def create_order(self, items):
        self.orders.append(items)


e1 = ECommer()
u1 = User("sat", "user")
p1 = Products(1, "aa", 100, 10)
p2 = Products(2, "bb", 200, 5)
cart1 = Cart(123)

e1.create_product(p1)
e1.create_product(p2)

print("PRODUCT LIST :", e1.products)
cart_list = e1.add_item_in_cart()




    


