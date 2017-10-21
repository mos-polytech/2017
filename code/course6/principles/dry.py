# -*- coding: utf-8 -*-

__author__ = 'sobolevn'

def print_info(self, info):
    d = open_file_stream()
    d.buffer()
    d.seek()
    d.flush()
    d.write(info)
    d.flush()
    d.close()


# First example:
class Iron(object, PrintableMixin):
    def say(self):
        print_info('I am a person!')


class Teacher(object, PrintableMixin):
    def print_info(self, info):
        print('before')
        super().print_info(info)

    def tell_about_yourself(self):
        self.print_info('I am a teacher!')


# Second example:
class Square(object):
    def __init__(self, size):
        self.height = size
        self.width = size
        print('Area is %d' % (self.height * self.width))

    def __str__(self):
        return 'Square with area: %d' % (self.width * self.height)


# Third example:
def calc(items):
    items_len = len(items)
    items_sum = sum(items)
    diff = items_sum / items_len

    return -diff


def print_stats(numbers):
    numbers_len = len(numbers)
    numbers_sum = sum(numbers)
    proportion = (numbers_sum / numbers_len) * 8 + (2 ** 3)

    return proportion / (numbers_len - numbers_sum)


if __name__ == '__main__':
    # 1:
    Person().say()
    Teacher().tell_about_yourself()

    # 2:
    print(Square(4))

    # 3:
    print(calc([1, 3, 9]))
    print(print_stats([0, 4, 5]))
