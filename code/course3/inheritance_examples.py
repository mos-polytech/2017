# -*- coding: utf-8 -*-


# All classes have the smae base class: object

class Test:
    pass


class Test(object):  # it is the same as the code above (py3 only)
    pass


# Classes can inherit other classes

class Person(object):
    biological_name = 'homo sapiens'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print('Walking...')

    def say_hello(self):
        print('I am a person', self.name, self.age)


class Student(Person):
    def say_hello(self):
        print('I am a student', self.name, self.age)


s = Student('Petr', 23)
print(s.biological_name)
s.walk()
s.say_hello()


class Child(Person):
    def walk(self):
        raise ValueError('Can not walk')

    def say_hello(self):
        raise ValueError('Can not talk')

    def crawl(self):
        print('Haha!')

child = Child('Steve Jr', 1)
print(child.biological_name)
