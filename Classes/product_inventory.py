"""
Product Inventory Project - Create an application which manages
an inventory of products. Create a product class which has a
price, id, and quantity on hand. Then create an inventory class
which keeps track of various products and can sum up the inventory
value.
"""

class Product(object):

    def __init__(self, price, id, qty, name):
        self.price = price
        self.id = id
        self.qty = qty
        self.name = name
        
    def update(self, amount):
        product += amount
        
class Inventory(object):
    
    def __init__(self):
        self.products = []
        
    def add(self, product):
        self.products.append(product)
        
    def printInventory(self):
        value = 0
        for p in self.products:
            print  p.name
            print 'Price: $%.2f' % round(p.price, 2)
            print 'ID: %d' % p.id
            print 'Qty: %d\n' % p.qty
            value += (p.price * p.qty)
            
        print 'Total value $%.2f' % round(value, 2)
            
if __name__ == '__main__':
    skittles = Product(.99, 1, 5, 'Skittles')
    MandMs = Product(.89, 2, 10, 'M&Ms')

    stuff = Inventory()
    stuff.add(skittles)
    stuff.add(MandMs)
    
    stuff.printInventory()