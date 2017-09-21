# -*- coding: utf-8 -*-


class Parent(object):
    def __init__(self):
        print('Parent inited')
        self.value = 'Parent'

    def do(self):
        print('Parent do(): {}'.format(self.value))


class Child(Parent):
    def __init__(self):
        print('Child inited')
        self.value = 'Child'


parent = Parent()
parent.do()

child = Child()
child.do()
