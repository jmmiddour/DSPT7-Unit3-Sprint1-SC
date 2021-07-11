from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    '''
    This function will generate a list of random products,
    based on the number of products (num_products) you enter.
    This is set to 30 products by default.
    '''
    products = []
    for _ in range(num_products):
        name1 = sample(ADJECTIVES, 1)[0]
        name2 = sample(NOUNS, 1)[0]
        name = name1 + ' ' + name2
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        products.append(Product(name, price=price, weight=weight, flammability=flammability))
    
    return products

# print(products)

def inventory_report(products):
    '''
    Prints a nice looking report of your product list.
    '''
    names = set()
    total_price = 0
    total_weight = 0 
    total_flammability = 0
    for val in products:
        names.add(val.name)
        total_price += val.price
        total_weight += val.weight
        total_flammability += val.flammability

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {len(names)}')
    print(
        f'Average price: ${total_price / len(products):.2f}')
    print(
        f'Average weight: {round(total_weight / len(products))}')
    print(
        f'Average flammability: {round(total_flammability / len(products), 1)}')


if __name__ == '__main__':  #
    inventory_report(generate_products())
