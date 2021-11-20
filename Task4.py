# Create a function that checks that the string given as an argument is a
# palindrome (ie read backwards and forwards is exactly the same, eg
# "kayak", "madam").

string = 'savas'
if string == string[::-1]:
    print('palindrome')
else:
    print('not palindrome')