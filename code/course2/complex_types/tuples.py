# -*- coding: utf-8 -*-

simple_tuple = (1, 2, 3, 4, 5)
print(simple_tuple)

# operations

# add
simple_tuple += (6, )
# simple_tuple = simple_tuple + (6, )
print(simple_tuple)









# tuples:
# TUPLES ARE IMMUTABLE!
empty_tuple = tuple()  # show __builtin__
tuple1 = (1, )
tuple2 = (1, )
not_a_tuple = (1)  # this is not a tuple!

print(
	tuple1 == tuple2, 
	tuple2 == not_a_tuple, 
	type(not_a_tuple), 
	not_a_tuple
)
print( (1, 2) == (1, 2, ) )



# tuple operations:

# add:
tuple1 = tuple1 + tuple2
print(tuple1)

tuple1 = (2, ) + tuple1 + (not_a_tuple, )
print(tuple1)

# indexing:
print(1 in tuple1, 2 in tuple1)

print(len(tuple1), len(tuple2), len(empty_tuple))
print(tuple2[0], tuple1[0:2], tuple1[:-1])

# tuple1[0] = "you can assign to tuple's items! they are read-only."
print(tuple1)


# removing:
# There's no direct way to delete an element from the tuple:
tuple1 = (1, 2, 'string', 'one more', False, None )
print(tuple1)

new_tuple = tuple()
for item in tuple1:  # tuple is iterable
    # we will remove all the 'strings' from tuple1
    # if not isinstance(item, (str, unicode)):  # or `basestring`
    if not isinstance(item, str):
        new_tuple += (item, )
print(new_tuple)



# nested:
print( (1, ('a', (tuple(), ), 'b'), 2, ) )

# multiply:
print(tuple2 * 3)








# unpack:
var1, var2 = ('foo', 'bar', )
print(var1, var2)

useful, _ = ('useful', 'this is not used', )
print(useful)

# These two examples are impossible:
# var1, var2, none_var = (1, 2, )
# var1, var = (1, 2, 3, )

# next: complex_types/lists.py
