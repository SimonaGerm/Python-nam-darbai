# Write a function that takes two strings and checks to see if they are
# anagrams of each other.
# For example:
# "Army" and "Mary",
# "Sharing" and "Sunday",
# "Quid est veritas?" and "Vir est qui adest",
# "Jim Morrison" and "Mr. Mojo Risin"
# "Tom Marvolo Riddle" and "I am Lord Voldemort"


def is_anagram(word1, word2):
    if sorted(word1.lower()) == sorted(word2.lower()):
        return 'is anagram'
    else:
        return 'not anagram'


if __name__ == '__main__':

    print(is_anagram('mary', 'army'))