# -*- coding: utf-8 -*-

GLOBAL_VALUE = 2


def do_work(value):
    return GLOBAL_VALUE * value + 2


def change_var(x):
    global GLOBAL_VALUE
    GLOBAL_VALUE = x


class Calc:
    def __init__(self, param):
        self.param = param

    def do_work(self, value):
        return self.param * value + 2

    def change_var(self, x):
        self.param = x
