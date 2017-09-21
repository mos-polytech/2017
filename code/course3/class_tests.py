
class Example:
    a = 1
    _b = 2
    __c = 3

class NewClass(Example):
    def __init__(self):
        print(self.a, self._b, self.__c)


n = NewClass()
print(n.a, n._b, n.__c)
