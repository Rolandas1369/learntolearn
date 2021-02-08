# Print within line of effect
data = [
    {'name': 1, 'b': 2, 'c': 4},
    {'name': 9, 'b': 3, 'c': 5},
    {'name': 1, 'b': 8, 'c': 4},
]
string_data = 'aa'

from operator import itemgetter, attrgetter
rows_by_name = sorted(data, key=itemgetter('name'))
print('sorted by name', rows_by_name)
print('min with itemgetter from dict', min(data, key=itemgetter('b')))

print(sorted(data, key=lambda val: val['name']))

rows_by_name = sorted(data, key=itemgetter('name'))

print('Get atribute of structure', attrgetter(string_data))

class Car:
    def __init__(self):
        self.data = 'aa'

new_car = Car()
print(attrgetter(new_car.data))

from operator import itemgetter
from itertools import groupby

data1 = [
    {'name': 'rol', 'b': 2, 'c': 4},
    {'name': 'bol', 'b': 3, 'c': 5},
    {'name': 'rol', 'b': 8, 'c': 4},
    {'name': 'bol', 'b': 2, 'c': 4},
    {'name': 'rol', 'b': 3, 'c': 5},
    {'name': 'bol', 'b': 8, 'c': 4},
]

# Sort group dictionary
for name, items in groupby(sorted(data1, key=itemgetter('c')), key=itemgetter('c')):
    print(name)
    for i in items:
        print(i)

# End in 44
