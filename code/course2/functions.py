# -*- coding: utf-8 -*-

# Step 0:

# Here we define a function:
def this_functions_prints_stars():
    print('I will print stars!')
    print('**********')

# Here we call the function:
this_functions_prints_stars()


# Step 1:
def my_function(input_var1, input_var2):
    print(input_var1, input_var2)  
    return input_var1 + input_var2

first_call = my_function(1, 1)
print(first_call)

second_call = my_function(1, 123)
print(second_call)


# Step 2:
def my_function(var1, var2, var3):
    print("No way I'm using this: {}, {}, {}".format(var1, var2, var3))

# my_function now is redefined to accept 3 arguments:
new_call = my_function(1, 2, 3)
print(new_call)


# Step 3:
def function_with_default_value(name, age=0, needs_stars=False):
    message = '{} is {} years old!'.format(name, age)
    print(message)

    if needs_stars:
        print('*****')

function_with_default_value('Nikita')
function_with_default_value('Alex', age=19)
function_with_default_value('Bob', age=40, needs_stars=True)


# Step 4:
def named_values(name=None, surname=None, patronimic=None):
    print('Full name: {} {} {}'.format(surname, name, patronimic))

named_values(name='Nikita', surname='Sobolev', patronimic='Andreevich')
named_values(surname='Petrov', patronimic='Ivanovich', name='Ivan')
named_values(surname='Semenov', name='Petr', patronimic='Ivanovich')


## Complex examples

# Complex step 1:
def sum_all(*args):
    print(args, type(args))

    result = 0
    for arg in args:
        result += arg
    return result

print(sum_all(1, 2, 3, 4, 5))

# Complex step 2:
def factorial(n):  # This function is recursive, it calls itself.
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(4))  # 4 * 3 * 2 * 1 = 24


# Complex step 3:
def do_callback(function, argument):  # you can pass functions as an arguments
    return function(argument)  # this is called "callback"

result = do_callback(len, 'string')
print(result)


# Complex step 4:
def all_together(value, *args, **kwargs):
    message = kwargs.pop('message', 'default message')
    if value > sum(args):
        print(message)
    else:
        print('value is not bigger than sum(args)')

all_together(1, 0)
all_together(1, 2, 3, 4)
all_together(5, 1, 1, 2, message='Done!')


# Complex step 5:
def enclosing(value):
    def _inner():
        print('value: {value}, new_value: {new_value}'.format(
            new_value=new_value, value=value,
        ))

    new_value = str(value * 10) * 2
    _inner()
    return new_value

enclosing(25)


# Complex step 6:
def decorator(function):
    def _inner(value):
        print(function(value))

    print('called')
    return _inner

decorated = decorator(len)
decorated([1, 2, 3])
