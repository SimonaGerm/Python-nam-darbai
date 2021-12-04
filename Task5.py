# Create a function that will calculate the number of upper and lower case
# letters in a string.
# eg for: "The quick Brown Fox"
# expected result:
# Number of uppercase letters: 3, number of lowercase letters : 13
# Hint: use a loop, conditional statement, and appropriate methods for the string


def count_lower_upper(sentence):
    lower_case = 0
    upper_case = 0
    for case in sentence:
        if case.isupper():
            upper_case = upper_case + 1
        elif case.islower():
            lower_case = lower_case + 1
    return upper_case, lower_case


if __name__ == '__main__':

    sentence = 'The quick Brown Fox'
    print(count_lower_upper(sentence))
