"""Write a program that returns the absolute value of a number retrieved
from the user. The program should keep asking for this number until it is
correctly given.
Remember that the user may not always enter a numeric value, but may
also enter, for example, "cauliflower". Check what happens then and be
sure to handle exceptions."""

# veikiantis paprastas kodas


while True:
    try:
        print(abs(float(input(f'Enter your number: '))))
        break
    except ValueError as V:
        print(V, f'Error: It is not a number.')
        continue


"""Nepavyko aprašyti kaip funkcijos, gaunu klaidą, exception neveikia. Ką daryti kitaip?"""
# def absolute_value(number):
#     while True:
#         try:
#             print(abs(number))
#             break
#         except ValueError as V:
#             print(V, f'Error: It is not a number.')
#             continue
#
#
# if __name__ == '__main__':
#
#     number = abs(float(input(f'Enter your number: ')))

