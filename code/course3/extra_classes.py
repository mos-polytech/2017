
class Test(object):
    case = 'Study'

    def __init__(self, x, y):
        print('Test inited!', self, x, y)
        self.update(x, y)

    def update(self, x1, y1):
        self.x = x1
        self.y_value = y1


t = Test(34, 13)
t1 = Test(90, 2)

print(t.case == t1.case)
print(t, t1, t == t1)

print(t.x, t1.x, t.x == t1.x)

t.update(0, 0)
t1.update(1, 1)

print(t.x, t1.x)
