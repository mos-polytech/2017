# -*- coding: utf-8 -*-


def my_function():
    print('I am a function')


print(my_function)
print('Functions are objects', isinstance(my_function, object))


# You can use variables to store functions

test = my_function
test()


# You can do any actions with functions

my_list = []
my_list.append(my_function)
print(my_list)


# You can pass functions as parameters

def call_passed_function(incoming):
    print('Calling!')
    incoming()
    print('Called!')


call_passed_function(my_function)


# You can not call uncallable things:

try:
    d = 2
    d()  # but you can try
except TypeError as e:
    print('It is not a function', e)


# You can check if something could be called

print(callable(len), callable(45), callable(callable))


# You can return function from a function

def return_min_function():
    return min

test = return_min_function()
min_value = test(4, 5, -9, 12)
print('Min values is', min_value)
