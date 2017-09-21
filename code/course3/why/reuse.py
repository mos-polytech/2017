# -*- coding: utf-8 -*-


def main_function(obj):
    param = 34
    return obj.do_something(param)


class SomeOldLogic:
    def do_something(self, value):
        x = self.calc(value)
        print('X is calculated!', x)

        print('A lot of work is done here!')

        x += 45
        if x < 0:
            x = 0
        x = x * 1.2

        return x

    def calc(self, value):
        return value * 7 + 90

x = SomeOldLogic()
main_function(x)


class NewLogic(SomeOldLogic):
    def calc(self, value):
        return value - 2

y = NewLogic()
main_function(y)
