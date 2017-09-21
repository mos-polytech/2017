
# Functions can be nested

def pretty_print(arg):
    def print_stars():
        print('-' * 8)
        print('*' * 8)

    print_stars()
    print(arg)
    print_stars()

pretty_print(12)


# Can 
