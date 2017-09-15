import sys  # importing the standart library `sys`.


# ints:
print('size of 0 = ', sys.getsizeof(0))  # 24
print('size of 1 = ', sys.getsizeof(1))  # 24 vs 28
print('size of 1000000 = ', sys.getsizeof(1000000))  # 24 vs 28

# max_int:
print('size of max_int - 1 = ', sys.getsizeof(sys.maxsize - 1))
print('size of max_int = ', sys.getsizeof(sys.maxsize))

"""
python2
('size of max_int - 1 = ', 24)
('size of max_int = ', 24)

python3
size of max_int - 1 =  36
size of max_int =  36
"""

# floats:
print('size of 0.0 =', sys.getsizeof(0.0))
print('size of 1.0 =', sys.getsizeof(1.0))

# mixed:
print('size of int(max_int + 1) = ', sys.getsizeof(int(sys.maxsize + 1)))
print('size of float(max_int + 1) =', sys.getsizeof(float(sys.maxsize + 1)))

# bools:
print('size of True = ', sys.getsizeof(True))

# None
print('size of None = ', sys.getsizeof(None))
