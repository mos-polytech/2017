# -*- coding: utf-8 -*-


# Functions can use global variables

GLOBAL_VAR = 3


def using_global_var(x):
    print(x * GLOBAL_VAR)

using_global_var(12)

# But if we want to write to it, we should state it explicitly

def writing_to_global_var(value):
    global GLOBAL_VAR
    GLOBAL_VAR = value
    print('it is now', GLOBAL_VAR)

writing_to_global_var(9)


# Functions are objects and can be nested

def outer_function(value):
    def some_inner():
        print('Value was', value)
    return some_inner

v = outer_function('some')
print('it is a function', v, callable(v))
v()  # 'some' will be printed






