class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return "Cheese(%r)" % (self.kind)

import weakref 

stock = weakref.WeakValueDictionary()
print(stock, type(stock))
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese

print(sorted(stock.keys()), stock.keys())
print(1111, cheese)
print("keys: ", sorted(stock.keys()))
del catalog
print("keys: ", sorted(stock.keys()))
print(2222, cheese)

del cheese
print(sorted(stock.keys()))
