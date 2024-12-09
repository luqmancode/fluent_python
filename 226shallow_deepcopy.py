from copy import copy, deepcopy

class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, passenger):
        self.passengers.append(passenger)

    def drop_pass(self, passenger):
        self.passengers.remove(passenger)

bus1 = Bus(['Alice', 'Spring', 'Bob', 'Martin'])
bus2 = copy(bus1)
bus3 = deepcopy(bus1)

print(id(bus1), id(bus2), id(bus3))
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))

# print(dir(bus1))
bus1.pick('mOhamed')
print(bus1.passengers, bus2.passengers, bus3.passengers)
bus1.drop_pass('Bob')
print(bus1.passengers, bus2.passengers, bus3.passengers)

