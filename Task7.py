# Write a function that will return the 5 most common words from
# Mickiewicz's work. https://pastebin.com/raw/aAHeW5Pt (copy and save
# to a text file what you will find at this link).
# Hint: use the open() function, split() method, dictionary and loop.

from collections import Counter

# TODO: Kažkas negerai, ne tą gauti tikėjausi, gauti fragmentai

with open('fileND.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    words = content.split()
    word_count = Counter(words)
    print(word_count.most_common(5))

# result =  [('w', 9), ('się', 6), ('z', 5), ('do', 5), ('A', 5)]
