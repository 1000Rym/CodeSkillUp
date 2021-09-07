from abc import ABC, abstractclassmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price 
    
    def total(self):
        return self.price * self.quantity


class Order: # The Context
    
    def __init__(self, customer, cart, promotion = None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self): 
        if not hasattr(self, '__total'):
            self.__total =  sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None :
            discount = 0
        else: 
            discount = self.promotion.discount(self)
        return self.total() - discount


    def __repr__(self):
        fmt = '<Order total : {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

class Promotion(ABC): # The strategy : Abstract Base Class

    @abstractclassmethod
    def discount(self, order):
        """Return discount as a positive dollar amount"""

class FidelityPromo(Promotion): # Concrete Strategy1
    """ 5 % discount for custommers with 1000 or more fidelity points"""
    
    def discount(self, order):
        return order.total()*.05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromo(Promotion):
    """10 % discount for each lineitem with 20 or more units"""
    
    def discount(self, order):
        return sum([item.total()*.1 for item in order.cart if item.quantity>=20])

class LargeOrderPromo(Promotion):
    """ 7% discount for orders with 10 or more distict items"""
    
    def discount(self, order):
        distict_items = {item.product for item in order.cart}
        return order.total() * .07 if len(distict_items)>=10 else 0



if __name__ == '__main__':
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5),
    LineItem('apple', 10, 1.5),
    LineItem('watermellon', 5, 5.0),
    LineItem('banana', 30, .5)]
    print(f'Fidelity Joe: {Order(joe, cart, FidelityPromo())}')
    print(f'Fidelity Ann: {Order(ann, cart, FidelityPromo())}')
    print(f'BulkItem: {Order(joe, cart, BulkItemPromo())}')
    long_order = [LineItem(str(item_code), 1, 1) for item_code in range(10)]
    print(f'LargeOrder:{Order(joe, long_order, LargeOrderPromo())}')
