# -*- coding: utf-8 -*-


# You can call parent's methods from child

class Parent:
    def print_info(self):
        print('Some info')


class SomeChild(Parent):
    def print_info(self):
        super().print_info()
        print('Some other info')

s = SomeChild()
s.print_info()

