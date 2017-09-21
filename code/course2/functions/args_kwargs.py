 # -*- coding: utf-8 -*-


# Functions can receive keyword arguments

def has_keywords(my=True, name='computer')
    if my:
        print('My', name)
    else:
        print('Not mine', name)


has_keywords(name='phone')


# Function can receive unlimited number of positional arguments

def has_args(*args):
    print('A lot of arguments: ', args)

has_args(1, 'demo', [1, 2], (9, 'string'))


# Functions can receive unlimited number of keyword arguments

def has_kwargs(**kwargs):
    print('A lot of keyword arguments', kwargs)
    print('kwargs is a dict', type(kwargs))

has_kwargs(any_possible=None, values=[], you_wish=1)


# Function that will cover 100% of arguments

def send_anything(*args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)

send_anything(1, 15, 'a', value=True, new_value=False)
