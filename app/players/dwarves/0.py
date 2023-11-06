class Square:
    def __init__(self, length, color=None):
        self.length = length
        self.color = color

    @property
    def area(self):
        return self.length ** 2


my_square = Square(5)

my_square.color = "Purple"
my_square.length = 6
my_square.area = 25

print(my_square.color, my_square.length, my_square.area)