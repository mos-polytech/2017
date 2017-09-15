# Infinitive loop:
while True:
    users_input = input('Please, input positive number: ')
    if float(users_input) > 0:
        print('Your number is: %s' % users_input)
        break
    else:
        print('%s is a wrong number.' % users_input)
        continue


















# Iterating over a chars in the string:
for char in '123456789':
    print(int(char) + 100)





