# ---------------------------
# User Class
# ---------------------------

class User:
    """
    Represents a customer in the ecommerce system
    """

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User({self.id}, {self.name})"


# ---------------------------
# Product Class
# ---------------------------

class Product:
    """
    Represents a product that can be purchased
    """

    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, qty):
        """
        Reduce product stock when order is placed
        """
        if qty > self.stock:
            raise Exception("Not enough stock")

        self.stock -= qty

    def __repr__(self):
        return f"Product({self.id}, {self.name}, price={self.price}, stock={self.stock})"


# ---------------------------
# CartItem Class
# ---------------------------

class CartItem:
    """
    Represents an item inside the cart
    """

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        """
        Calculate total price of this item
        """
        return self.product.price * self.quantity


# ---------------------------
# Cart Class
# ---------------------------

class Cart:
    """
    Cart belongs to a user and contains multiple items
    """

    def __init__(self, user):
        self.user = user
        self.items = []

    def add_item(self, product, qty):
        """
        Add product to cart
        """

        if product.stock < qty:
            raise Exception("Product out of stock")

        # check if product already exists
        for item in self.items:
            if item.product.id == product.id:
                item.quantity += qty
                return

        self.items.append(CartItem(product, qty))

    def remove_item(self, product_id):
        """
        Remove item from cart
        """
        self.items = [item for item in self.items if item.product.id != product_id]

    def view_cart(self):
        return self.items


# ---------------------------
# Order Class
# ---------------------------

class Order:
    """
    Represents a placed order
    """

    def __init__(self, user, items):
        self.user = user
        self.items = items
        self.total = self.calculate_total()

    def calculate_total(self):
        """
        Calculate order total
        """

        total = 0

        for item in self.items:
            total += item.get_total_price()

        return total

    def __repr__(self):
        return f"Order(user={self.user.name}, total={self.total})"


# ---------------------------
# Payment Class
# ---------------------------

class Payment:
    """
    Handles payment processing
    """

    def __init__(self, order):
        self.order = order
        self.amount = order.total
        self.status = "PENDING"

    def process_payment(self):
        """
        Simulate payment processing
        """

        self.status = "SUCCESS"
        print("Payment successful for amount:", self.amount)


# ---------------------------
# Ecommerce System
# ---------------------------

class EcommerceSystem:
    """
    Main system managing users, products and orders
    """

    def __init__(self):
        self.users = []
        self.products = []
        self.orders = []

    def add_user(self, user):
        self.users.append(user)

    def add_product(self, product):
        self.products.append(product)

    def place_order(self, cart):

        # create order
        order = Order(cart.user, cart.items)

        # reduce product stock
        for item in cart.items:
            item.product.reduce_stock(item.quantity)

        # process payment
        payment = Payment(order)
        payment.process_payment()

        self.orders.append(order)

        # clear cart
        cart.items = []

        return order


# ---------------------------
# Main Execution
# ---------------------------

if __name__ == "__main__":

    system = EcommerceSystem()

    # create user
    user1 = User(1, "Rama", "rama@email.com")
    system.add_user(user1)

    # create products
    p1 = Product(1, "Laptop", 50000, 10)
    p2 = Product(2, "Mouse", 500, 50)

    system.add_product(p1)
    system.add_product(p2)

    # create cart
    cart = Cart(user1)

    cart.add_item(p1, 1)
    cart.add_item(p2, 2)

    print("Cart Items:", cart.view_cart())

    # place order
    order = system.place_order(cart)

    print(order)

    print("Remaining stock:", p1.stock, p2.stock)