# CTRL+ALT+SHIFT_L
# iterable
x = [1, 2, 3, 4]
z, *b, y = x
print(z, *b, y)
print(sum(b))
from collections import deque

de = deque(x)
de.append(1)
de.append(1)
print(de, len(de), f'counts item of in de {de.count(1)}')
de_limit = deque(x, maxlen=3)
print('Removes first leaves last', de_limit)
[print(x) for x in de_limit]
# new object of deque
new_de = deque()
# append new data rules as in list
new_de.append({1, 2, 3})
# array shift
new_de.appendleft([1])
print(new_de)

import heapq

# find largest ant smallest from list
l1 = [1, 2, 3, 4]
largest_in_list = heapq.nlargest(2, l1)
smallest_in_list = heapq.nsmallest(2, l1)
print(largest_in_list, smallest_in_list)

struct = [{'a': 1, 'b': 4}, {'a': 1, 'b': 6}, {'a': 7, 'b': 9}, {'a': 7, 'b': 9}]
# return list of n dicts where key is largest
largerst_from_inerr_dict = heapq.nlargest(2, struct, key=lambda list_dict: list_dict['b'])
print(largerst_from_inerr_dict)
struct1 = [10, 2, 3, 4, 5]
# convert list to heap
heapq.heapify(struct1)
# removes smallest value 2
print(heapq.heappop(struct1))
print(struct1)
struct2 = [1, 2, 3, 4]
heapq.heapify(struct2)
# pushes to heap preserves order
print(heapq.heappush(struct2, 3))
print(struct2)
from collections import defaultdict

d = defaultdict(list)
d['a'] = 1
d['b'] = 2
print(d['a'])
set_dict = defaultdict(set)
# create set dict
set_dict['a'] = {1, 5}
# updates by last value reasigns
set_dict['a'] = {1, 2}
set_dict['b'] = {2, 3}
# append to inerr set
set_dict['a'].add(6)
print(set_dict)
cc = defaultdict(dict)
cc['somethin'] = {'a': 1}
print(cc)

multi_params = (('a', 1), ('b', 2))

dict_from_multiple_params = defaultdict(list)
for key, value in multi_params:
    dict_from_multiple_params[key] = value
print(dict_from_multiple_params)

from collections import OrderedDict

# cant see differences in ordered and unordered dicts
ordered_dict = OrderedDict()
ordered_dict['s'] = 4
ordered_dict['c'] = 2
ordered_dict['g'] = 5
print(ordered_dict)

unordered_dict = {}
unordered_dict['d'] = 1
unordered_dict['c'] = 5
unordered_dict['f'] = 8
unordered_dict['z'] = 3
unordered_dict['l'] = 9

print(unordered_dict)

new_dict = {}
for key, value in zip(['a', 'c', 'b'], [2, 8, 1]):
    new_dict[key] = value
print(new_dict)

new_ordered_dict = OrderedDict()
for key, value in zip([10, 2, 3], [2, 8, 1]):
    new_ordered_dict[key] = value
print(new_ordered_dict)
for i in new_ordered_dict:
    print(i)
# zip can only be accessed once
c = zip([1, 2, 3], [1, 2, 3])
print('first access')
[print(x) for x in c]
print('second access gives nothing')
[print(j) for j in c]

prices = {'c': 1, 'a': 2, 'b': 3, 'f': 4}
# min max from dict
print(min(zip(prices.keys(), prices.values())))
print(max(zip(prices.keys(), prices.values())))
# sort by value
print(sorted(zip(prices.values(), prices.keys())))
# sort by key
print(sorted(zip(prices.keys(), prices.values())))
print(sum(prices.values()))
# key of max from dict
print(max(prices.keys(), key=lambda k: prices[k]))
# max value from dict
print(max(prices.values(), key=lambda k: k))
print(max(prices))
# in duplicated keys min/max determened by key value
# common/uncommon dicts
a = {'a': 1, 'b': 2}
b = {'c': 1, 'b': 2}
print(a.keys() & b.keys())
# key not in b
print(a.keys() - b.keys())
# keys not in a
print(b.keys() - a.keys())
print(a.items() & b.items())

mult_dict_values = {'a': 1, 'b': 2, 'c': 4, 'd': 5}
without_ab = {key: mult_dict_values[key] for key in mult_dict_values.keys() - {'a', 'b'}}
print(without_ab)
# dict from tuple
a = (('a', 1), ('b', 2), ('c', 3))
tuple_dict = {c[0]: c[1] for c in a}
print(tuple_dict)
removable_keys = {'a', 'b', 'c'} - {'a'}
print(removable_keys)

p = [1, 2, 5, 1, 3, 1]
print(list(set(p)))

# LOOK AGAIN
c = [{'a': 1, 'b': 1}, {'a': 2, 'b': 2, 'e': 1}, {'a': 2, 'b': 2, 'f': 1}, {'a': 1, 'b': 1}]


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


g = list(dedupe(c, key=lambda ie: (ie['a'])))
print(g)
az = [{'x': 1, 'y': 2}, {'x': 1, 'y': 2}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
remove_dupls = list(dedupe(az, key=lambda d: (d['x'], d['y'])))
remove_by_one = list(dedupe(az, key=lambda d: d['x']))
print(remove_by_one, remove_dupls)
print({'a': 1} == {'a': 1})
# slice list
a = [1,2,3]
SLICE = slice(1, 2)
print(a[SLICE])
a[SLICE]=[5]
print(a)
del a[SLICE]
print(a)

from collections import Counter

dupl_list = ['a', 'b', 'c', 'd', 'a']
dupl_list1 = ['a', 'b', 'c', 'd', 'a']
one_counted = Counter(dupl_list)
one_counted1 = Counter(dupl_list)
# can count counter
print(one_counted + one_counted1)

