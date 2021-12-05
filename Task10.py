"""Write a program that returns the absolute value of a number retrieved
from the user. The program should keep asking for this number until it is
correctly given.
Remember that the user may not always enter a numeric value, but may
also enter, for example, "cauliflower". Check what happens then and be
sure to handle exceptions."""

# veikiantis paprastas kodas


# while True:
#     try:
#         print(abs(float(input(f'Enter your number: '))))
#         break
#     except ValueError as V:
#         print(V, f'Error: It is not a number.')


def absolute_value():
    while True:
        try:
            print(abs(float(input(f'Enter your number: '))))
            break
        except ValueError as V:
            print(V, f'Error: It is not a number.')


if __name__ == '__main__':

    absolute_value()

