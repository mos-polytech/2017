# -*- coding: utf-8 -*-


# Constructor is called when new instance is created

class TestClass:
    def __init__(self):
        print('Constructor is called!')
        print('Self is the object itself!', self)

t = TestClass()
t1 = TestClass()


# Constructor can have parameters

class Table:
    def __init__(self, number_of_legs):
        print('New table has {} legs'.format(
            number_of_legs))

t = Table(4)
t1 = Table(3)


# But we need to save them into the fields!

class Chair:
    def __init__(self, color):
        self.color = color

c = Chair('green')
print(c, c.color)

c1 = Chair('Red')
print(c1.color)
print('varibale c did not change!', c.color)
