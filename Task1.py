# Task 1
# Write a program that will convert the sequence of numbers entered by
# the user into text, e.g .:
# 112 -> "one one two"
# 9973 -> "nine nine seven three"
# Hint: you need the input () function, a dictionary and a loop

numword = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 0 : 'zero'}

number = list(input('Insert your number: '))

ints = []
for num in number:
    ints.append(int(num))
for element in ints:
    print(numword[element], end=' ')


