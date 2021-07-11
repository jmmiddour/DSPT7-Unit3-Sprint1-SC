
import random


class Product:
    """
    Creates a Class for different attributes of a Product.

    Args:   name         : (str) The name of the product.
            price        : (int) The price of the product.
                            (default == 10)
            weight       : (int) The weight of the product.
                            (default == 20)
            flammability : (float) The flammability of the product.
                            (default == 0.5)
            identifier   : (int) The number to  identify the product.
                            (default == random int 1000000 to 9999999)
    """
    # Initialise a class variable:
    counter = 0

    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

        # Increase the class variable by 1 when new object is created:
        Product.counter += 1

    def stealability(self):
        stealable = self.price / self.weight
        if stealable < 0.5:
            print('Not so stealable...')
        elif 0.5 <= stealable < 1.0:
            print('Kinda stealable.')
        else:
            print('Very stealable!')

    def explode(self):
        explodable = self.flammability * self.weight
        if explodable < 10:
            print('...fizzle.')
        elif 10 <= explodable < 50:
            print('...boom!')
        else:
            print('...BABOOM!!')

    def __repr__(self):
        return '%s, %s, %s, %s, %s' % (
            self.name, self.price, self.weight, self.flammability, self.identifier)


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        super().__init__(name, price, flammability, identifier)
        self.weight = weight

    def explode(self):
        print("...it's a glove.")

    def punch(self):
        if self.weight < 5:
            print("That tickles.")
        elif 5 <= self.weight < 15:
            print("Hey that hurt!")
        else:
            print("OUCH!")
