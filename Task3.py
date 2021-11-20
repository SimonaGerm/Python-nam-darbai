# Create a function that checks that the number given in the argument is
# prime. The function should take a numeric value and return a logical
# value of True / False.
# E.g.
# For 11 the function will return True, for 12 -> False

number = 11
if number > 1:
    for value in range(2, int(number/2)+1):
        if (number % value) == 0:
            print('False')
            break
    else:
        print('True')
else:
    print('False')

