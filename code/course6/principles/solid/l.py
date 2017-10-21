# -*- coding: utf-8 -*-

__author__ = 'sobolevn'


class Rect(object):
    def __init__(self, w, h):
        self._width = w
        self._height = h

    def set_width(self, w):
        self._width = w

    def set_height(self, h):
        self._height = h

    def get_area(self):
        return self._height * self._width


class Square(Rect):
    def set_height(self, h):
        self._height = h
        self._width = h

    def set_width(self, w):
        self._height = w
        self._width = w


def return_object():
    return Square(1, 1)


if __name__ == '__main__':
    rect = return_object()
    rect.set_height(1)
    rect.set_width(4)

    print(rect.get_area())
    assert rect.get_area() == 4
