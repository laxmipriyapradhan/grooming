# Shopping Cart Class
class ShoppingCart:
    # Class Variables
    products = {'iPhone': 5, 'iMac': 3, 'iWatch': 2, 'iPad': 4}
    prices = {'iPhone': 800, 'iMac': 2500, 'iWatch': 3000, 'iPad': 3500}
    def __init__(self):
        self.cart = [ ]

    def add_item(self, name, quantity):
        if name not in self.__class__.products.keys():
            raise Exception('Product Not Available')
        elif self.__class__.products[name] >= quantity:
            self.cart.append({'name': name, 'price': self.__class__.prices[name], 'quantity': quantity})
            self.__class__.products[name] -= quantity
        else:
            raise ValueError('Product Out of Stock')

    def total_cost(self):
        return sum([item['price'] * item['quantity'] for item in self.cart])

    def remove_item(self, name):
        for item in self.cart:
            if name == item['name']:
                if item['quantity'] == 1:
                    self.cart.remove(item)
                else:
                    item['quantity'] -= 1

    def summary(self):
        print(f'{"name":>20} {"price":>20} {"quantity":>20}')
        print('−' * 65)
        for item in self.cart:
            print(f'{item["name"]:>20} {item["price"]:>20} $ {item["quantity"]:>20}')
            print('−' * 65)
            print(f'{"Total Cost:":>20}{self.total_cost():>20} $')
