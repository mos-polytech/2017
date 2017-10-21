# -*- coding: utf-8 -*-

import sys

try:
    from io import StringIO
except ImportError:
    from cStringIO import StringIO

__author__ = 'sobolevn'


class Printer(object):
    def write(self, message):
        sys.stdout.write(message + '\n')


class RefactoredPrinter(object):
    # def __init__(self, buffer):
    #     self.buffer = buffer

    def write(self, message, buffer):
        buffer.write(message)
        buffer.write(u'\n')


if __name__ == '__main__':
    Printer().write('This is right, but may be improved!')

    rfp = RefactoredPrinter()

    rfp.write('This is better', sys.stdout)
    rfp.write('This is error', sys.stderr)

    st = StringIO()
    rfp.write(u'here we go', st)
    print(st.getvalue())
