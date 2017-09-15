# String types:
print("This is a string.")
print('This is also a string.')

print('We are equal' == "We are equal")

print('Я русская строка.')

print("""
This string contains multiline
    text. And extra spaces.
""")







# Casting to string:
print(str(4))
print(str(4 + 1))
print(str(4) + '1')
print(str(None), str(True), str(False), str(object))










# String operations:
print('123' + '456')  # but it is impossiable to '123' - '3'
print('4' * 4)




print('Chars'[0], '123'[1], 'abc'[-1])


# Testing occurrence
print('be' in 'To be or not to be?')
print('123' in '123')
print('100' in '200')

print('I am not there' not in 'String')


# String format:
print('Hello, {}. You are learning {}'.format('Nikita', 'Python'))


# String length:
print(len('7 chars'))
