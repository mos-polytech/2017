# -*- coding: utf-8 -*-


# lists:
not_a_list = (1, 2)
list1 = [1, 2]
list2 = list(not_a_list)  # show __builtin__
# get the tuple back by: `new_tuple = tuple(list2)`

print(list1 == list2, not_a_list == list1)

# list operations:

# add:
# Note the difference between `.append()` and `+=` for tuples.
list1.append(3)
print('append() returns None: ', list1.append(4))
print(list1)

list1.append(list2)
print(list1)

list1.extend(list2)
print(list1)

list1.insert(1, 'inserted value')  # TODO: REMOVE INSERT
print(list1)

# LISTS ARE MUTABLE
# Switch to http://pythontutor.com/visualize.html#mode=edit
var = ['bar']
new_var = var
var.append('foo')
var[0] = 'baz'  # you can assign to items
print(new_var)  # try the same with `copy()`
# end








# delete:
test_list = ['pop', 'remove', 'del']

# by index:
popped = test_list.pop(0)
print('popped value is "{}"'.format(popped))

# by value:
test_list.remove('remove')

# or del it:
del test_list[0]  # del doesn't return a value









# unpack
v, s = ['v', 's']
print(v, s)


# multi-dimensional lists:
multi = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11]
]  # matrix 4*3

for row in multi:
    print(row)
    for element in row:
        print('element: ', element)


# generating lists: range() function
# xrange in 2.7 = range in 3
print('range', range(1, 10))

for i in list(range(1, 15, 2)):
    print(i)

# next: complex_types/dict.py
