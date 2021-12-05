""" Write two independent functions to solve the following problems:
     a) count_digits should count the number of integers that will be given as an argument,
     b) count_zeros should count the number of integers that will be given as an argument.
     Examples:
     >> x = count_digits (1234)
     >> print (x)
     4
     >> x = count_zeros (1000)
     >> print (x)
     3"""


def count_digits(digits):
    digits = int(digits)
    return len(str(digits))


def count_zeros(digits):
    counter = 0
    for digit in str(digits):
        if digit == '0':
            counter += 1
    return counter


if __name__ == '__main__':

    user_input = input('Enter your number: ')
    print(count_digits(1111))
    print(count_zeros(user_input))

