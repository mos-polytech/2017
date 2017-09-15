# -*- coding: utf-8 -*-


# Switch to http://pythontutor.com/visualize.html#mode=edit

# example 1:
my_list = [[1, 2], ['a', 'b']]
my_tuple = ('foo', 'bar', )

new_list = my_list
new_tuple = my_tuple

my_list.append([True, False])
my_tuple += ('baz', )

print(my_list, new_list)
print(my_tuple, new_tuple)















# Complex examples


import copy

# example 2:
var = {'list': [[1, 2], ['a', 'b']], 'tuple': ('foo', 'bar', )}
new_var = var.copy()
var.update({'str': 'string'})
var['list'].append([True, False])
var['tuple'] += ('baz', )

print(var)
print(new_var)


# example 3 (not supported by pythontutor) - debug:
var = {'list': [[1, 2], ['a', 'b']], 'tuple': ('foo', 'bar', )}
new_var = copy.deepcopy(var)
var.update({'str': 'string'})
var['list'].append([True, False])
var['tuple'] += ('baz', )

print(var)
print(new_var)
