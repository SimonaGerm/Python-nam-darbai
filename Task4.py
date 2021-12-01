# Create a function that checks that the string given as an argument is a
# palindrome (ie read backwards and forwards is exactly the same, eg
# "kayak", "madam").

def is_palindrome(string):
    if string == string[::-1]:
        return'palindrome'
    else:
        return 'not palindrome'


if __name__ == '__main__':

    print(is_palindrome('savas'))