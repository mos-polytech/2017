# -*- coding: utf-8 -*-


class Parent(object):
    def call(self):
        print('Parent')


class Child(Parent):
    def call(self):
        print('Child')


class Example(object):
    def call(self):
        print('Ex')


def call_obj(obj):
    obj.call()


def sum_two_objects(one, two):
    return one + two


call_obj(Child())
call_obj(Parent())







