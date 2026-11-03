class Product:

    def __init__(self, pid, name, price, stock):

        self.pid = pid
        self.name = name
        self.price = price
        self.stock = stock


class ShoppingCart:

    def __init__(self):

        self.cart = {}
        self.products = {}
        self.total = 0

    def add_product(self, pid, qty):

        if pid not in self.products:

            print("Product does not exist")

        elif qty <= 0:

            print("Invalid quantity")

        else:

            product = self.products[pid]

            if pid in self.cart:
                current = self.cart[pid]
            else:
                current = 0

            if current + qty <= product.stock:

                self.cart[pid] = current + qty

                print("Product added successfully")

            else:

                print("Insufficient stock")

    def remove_product(self, pid, qty):

        if pid not in self.cart:

            print("Product not in cart")

        elif qty <= 0:

            print("Invalid quantity")

        elif qty > self.cart[pid]:

            print("Cannot remove more quantity than available")

        else:

            self.cart[pid] = self.cart[pid] - qty

            if self.cart[pid] == 0:

                del self.cart[pid]

            print("Product removed successfully")

    def calculate_total(self):

        self.total = 0

        for pid in self.cart:

            product = self.products[pid]

            qty = self.cart[pid]

            amount = product.price * qty

            self.total = self.total + amount

        print("Total:", self.total)

    def display_cart(self):

        self.total = 0

        if len(self.cart) == 0:

            print("Cart is empty")

        else:

            for pid in self.cart:

                product = self.products[pid]

                qty = self.cart[pid]

                subtotal = product.price * qty

                self.total = self.total + subtotal

                print(product.name, "- Quantity:", qty,
                      "- Price:", product.price,
                      "- Subtotal:", subtotal)

        if self.total >= 20000:

            discount = 15

        elif self.total >= 10000:

            discount = 10

        elif self.total >= 5000:

            discount = 5

        else:

            discount = 0

        discount_amount = self.total * discount / 100

        final_amount = self.total - discount_amount

        print("Total Amount:", self.total)
        print("Discount:", str(discount) + "%")
        print("Discount Amount:", discount_amount)
        print("Final Amount:", final_amount)


# MAIN PROGRAM

n = int(input("Enter number of products: "))

shop = ShoppingCart()

for i in range(n):

    data = input("Enter product details: ").split()

    pid = int(data[0])
    name = data[1]
    price = int(data[2])
    stock = int(data[3])

    p = Product(pid, name, price, stock)

    shop.products[pid] = p


operations = int(input("Enter number of operations: "))

for i in range(operations):

    data = input("Enter operation: ").split()

    if data[0] == "ADD":

        pid = int(data[1])
        qty = int(data[2])

        shop.add_product(pid, qty)

    elif data[0] == "REMOVE":

        pid = int(data[1])
        qty = int(data[2])

        shop.remove_product(pid, qty)

    elif data[0] == "TOTAL":

        shop.calculate_total()

    elif data[0] == "DISPLAY":

        shop.display_cart()