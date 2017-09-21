# 1. Написать функцию, которая выбрасывает одно из трех исключений: ValueError, TypeError или RuntimeError случайным образом. В месте вызова функции обрабатывать все три исключения

import random


def raise_random_error():
    ex = random.choice([ValueError, TypeError, RuntimeError])
    raise ex('Message for a user')

try:
    raise_random_error()
except ValueError as e:
    print('Value', e)
except TypeError as e:
    print('Type', e)
except RuntimeError as e:
    print('Runtime', e)


# 2. Написать функцию, которая принимает на вход список, если в списке все объекты - int, сортирует его. Иначе выбрасывает ValueError

def sort_numbers(numbers):
    for num in numbers:
        if not isinstance(num, int):
            raise ValueError('{} is not a number'.format(num))

    numbers.sort()
    # Or:
    # if any(not isinstance(num, int) for num in int):


try:
    values = [1, 'a', 3]
    sort_numbers(values)
    print(values)
except ValueError as e:
    print(e)


# 3. Написать функцию, которая принимает словарь, преобразует все ключи словаря к строкам и возвращает новый словарь

def keys_to_str(data):
    result = {}
    for key, value in data.items():
        result[str(key)] = value
    return result

print(keys_to_str({1: 'one', None: True}))


# 4. Написать функцию, которая принимает список чисел и возвращает их произведение

def multiply_all(numbers):
    res = 1 
    for num in numbers:
        res *= num
    return res

print(multiply_all([3, 4, 2]))
