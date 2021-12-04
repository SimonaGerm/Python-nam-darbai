# Create a function that checks that the string given as an argument is a
# palindrome (ie read backwards and forwards is exactly the same, eg
# "kayak", "madam").


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
