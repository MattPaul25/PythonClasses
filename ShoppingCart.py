class ShoppingCart(object):
    """description of class"""
    def __init__(self):
        self.items = []

    def addItem(self, productName, price):
        item = (productName, price) #item is now a tuple
        self.items.append( item )

    def __iter__(self): #equivalent of implementing ienumerable (overidding iter method from object base class)
        return self.items.__iter__() 

    @property #decorates this method to make it a class level property
    def total_price(self):
        total = 0
        for i in self.items:
            total += i[1]
   
        return total

cart = ShoppingCart()

cart.addItem('car', 2000)
cart.addItem('fridge', 100)

for item in cart:
    print(type(item)) #prints the type of item (its a tuple) 
    print(item[0])  #prints the tuple at index of 0

print("Total Price is ${0}".format(cart.total_price))