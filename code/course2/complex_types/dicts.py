# -*- coding: utf-8 -*-

this_is_dict = {'key': 'value'}
this_is_also_dict = {'key': 'value'}

print(this_is_dict == this_is_also_dict)












# DICTS ARE MUTABLE!
# Switch to http://pythontutor.com/visualize.html#mode=edit
var = {1: 'value'}
new_var = var
var.update({2: 'new value'})
var[1] = 'mutated value'
print(new_var)  # try the same with `copy()`
# end


# operations with dicts:

# add:
this_is_dict.update({'name': 'Super Mario'})
print(this_is_dict)

# get:
print('Name is "{}"'.format(this_is_dict['name']))

print('Name is "{}"'.format(
    this_is_dict.get('name', 'Default Name'))
)

print('Address is "{}"'.format(
    this_is_dict.get('address', 'Default Address'))
)

# get only keys:
print(this_is_dict.keys())

# get only values:
print(this_is_dict.values())

# remove:
test_dict = {'pop-by-key': 1, 'pop-item': 2, 'to-del': 3}

del test_dict['to-del']
print(test_dict)

popped = test_dict.pop('pop-by-key')
print(popped)

missing = test_dict.pop('not-existing-key', 'default value')
print(missing)

popped = test_dict.popitem()
print(popped)

print(test_dict)

# iterate:
to_iterate = {1: 'x2', 2: 'x4', 3: 'x8'}
for key in to_iterate:
    print(key, to_iterate[key])

for key, value in to_iterate.items():
    print(key, value)

# clear:
to_clear = {'key': 'value', 1: 2}
to_clear.clear()
print(to_clear)


# string format:
print('{first_name}, {second_name}'.format(
    first_name='Clark', second_name='Kent',
))

# next: mutations.py
