# Susikuriu Dict:
numword = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 0 : 'zero'}


# # Pirmas metodas pasiimti reikšmes iš Dict:
# # TODO: Kaip išspausdinti žodžius be kabučių?
# keys = [1, 1, 2]
# values = list(map(numword.get, keys))
# print(values)
#
#
# keys2 = [9, 9, 7, 3]
# values2 = list(map(numword.get, keys2))
# print(values2)
#
#
# # TODO: Kaip išspausdinti žodžius ne stulpeliu, o viena eilute?
# # antras metodas pasiimti reikšmes iš Dict
# for key in keys:
#     print(numword.get(key))
#
# for key2 in keys2:
#     print(numword.get(key2))
#
#
# # trečias metodas pasiimti reikšmes iš Dict:
# pirmas = [numword.get(key) for key in keys]
# print(pirmas)
# # Arba:
#
# print([numword.get(key) for key in keys])
#
# antras = [numword.get(key2) for key2 in keys2]
# print(antras)
#
# print([numword.get(key2) for key2 in keys2])


# Task 1
# Write a program that will convert the sequence of numbers entered by
# the user into text, e.g .:
# 112 -> "one one two"
# 9973 -> "nine nine seven three"
# Hint: you need the input () function, a dictionary and a loop


number = list(input('Insert your number: '))

ints = []
for num in number:
    ints.append(int(num))
for element in ints:
    print(numword[element], end=' ')


