# Write a function that takes two strings and checks to see if they are
# anagrams of each other.
# For example:
# "Army" and "Mary",
# "Sharing" and "Sunday",
# "Quid est veritas?" and "Vir est qui adest",
# "Jim Morrison" and "Mr. Mojo Risin"
# "Tom Marvolo Riddle" and "I am Lord Voldemort"

word1 = 'army'
word2 = 'mary'
if sorted(word1) == sorted(word2):
    print('anagrams')
else:
    print('not anagrams')