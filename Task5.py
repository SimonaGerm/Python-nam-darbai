# Create a function that will calculate the number of upper and lower case
# letters in a string.
# eg for: "The quick Brown Fox"
# expected result:
# Number of uppercase letters: 3, number of lowercase letters : 13
# Hint: use a loop, conditional statement, and appropriate methods for the string

string = 'The quick Brown Fox'
upper_case = 0
lower_case = 0
for case in string:
    if (case.isupper()):
        upper_case = upper_case + 1
    elif (case.islower()):
        lower_case = lower_case + 1
print(f'upper: {upper_case}')
print(f'lower: {lower_case}')
