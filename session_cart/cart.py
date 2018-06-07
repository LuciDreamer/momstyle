import cart
import json
from momshop.models import Products
from decimal import Decimal
from momshop.models import Order


class CartItem(object):

    def __init__(self, product_id, size, quantity):
        self.product_id = product_id
        self.quantity = int(quantity)
        self.product = Products.objects.get(id=self.product_id)
        self.name = self.product.title
        self.price = str(self.product.price)
        self.size = str(size)

    def item_to_dict(self):
        item = {'product_id': self.product_id,
                'product_name': self.name,
                'quantity': self.quantity,
                'price': self.price,
                'size': self.size,
                }
        return item


class Cart(object):
    # session cart objects logic
    # adds, removes items, shows, cleans cart

    def __init__(self, request):
        # initializes cart object and saves it into session

        self.session = request.session

        if 'session_cart' in request.session:
            session_cart = request.session['session_cart']
            self.cart = session_cart
        else:
            session_cart = {}
            request.session['session_cart'] = session_cart
        self.cart = session_cart

    def update_session(self):
        self.session['session_cart'] = self.cart

    @property
    def items_list(self):
        items_list = []
        for item in self.cart.values():
            items_list.append(item)
        return items_list

    def make_name(self, product_id, size):
        name = 'product' + str(product_id) + str(size)
        return name


    def items_count(self):
        x = 0
        for item in self.items_list:
            x += 1
        return x


    def add_item(self, request, product_id, quantity, size):
        """
        creates new cartitem object with params from request and saves this object
        into the cart
        """
        if self.make_name(product_id, size) in self.cart.keys():
            print('item already in the cart we just change quantity')
            self.cart[self.make_name(product_id, size)]['quantity'] += int(quantity)
            self.update_session()
            print(self.items_list)
        else:
            cart_item = CartItem(product_id, size, quantity)
            self.cart[self.make_name(product_id, size)] = cart_item.item_to_dict()
            self.update_session()
            print(self.cart)


    def set_quantity(self, product_id, action, size):
        if action == 'increase':
            self.cart[self.make_name(product_id, size)]['quantity'] += 1
            self.update_session()

        else:
            self.cart[self.make_name(product_id, size)]['quantity'] += 1
            self.update_session()

    def clean_cart(self):
        # deletes all cart items from the session cart

        self.cart = {}
        self.update_session()

    def delete_item(self, product_id, size):
        self.cart.pop(self.make_name(product_id, size))
        print("item was deleted")
        self.update_session()

    def unique_items(self):
        return len(self.cart)

    @property
    def total_price(self):
        total_price = []
        for item in self.items_list:
            price = Decimal(item['price'])
            quantity = int(item['quantity'])
            total = price * quantity
            total_price.append(total)
        return sum(total_price)





