# Create a function that checks that the number given in the argument is
# prime. The function should take a numeric value and return a logical
# value of True / False.
# E.g.
# For 11 the function will return True, for 12 -> False


def prime_argument(number):
    if number > 1:
        for value in range(2, int(number/2)+1):
            if (number % value) == 0:
                return 'False'
        else:
            return 'True'
    else:
        return 'False'


if __name__ == '__main__':

    print(prime_argument(11))
