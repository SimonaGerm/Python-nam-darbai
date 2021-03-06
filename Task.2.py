# Create a function that takes a list of integers and returns what the
# smallest number is in.
# Do not use built-in functions.
# eg for the list [42, 13, 56, 7, 12, 3, 85] the function should return 5, because
# the smallest element is found at this index in this list.


def smallest(list):
    current_min = list[0]
    for num in list:
        if num < current_min:
            current_min = num
    return list.index(current_min)


if __name__ == '__main__':
    print(smallest([15, 52, 258, 125, 1, 658, 1000]))
