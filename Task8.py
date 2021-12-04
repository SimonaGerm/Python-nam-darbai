"""Create a Rectangle class whose attributes will be the height and width of
the figure. Implement methods to measure the perimeter and area of a
rectangle.
Then create a Square class, remembering that every square is a
rectangle, but not every rectangle is a square."""


# Rectangle Class:

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimeter(self):
        return (self.height + self.width) * 2

    def area(self):
        return self.height * self.width


class Square(Rectangle):
    def __init__(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height

    def set_w(self, width):
        self.width = width
        self.height = width


if __name__ == '__main__':

    rectangle_1 = Rectangle(5, 20)
    square_1 = Square(5)
    print(f'Rectangle perimeter is: {rectangle_1.perimeter()}')
    print(f'Rectangle area is: {rectangle_1.area()}')
    print(f'Square perimeter is: {square_1.perimeter()}')
    print(f'Square area is: {square_1.area()}')
