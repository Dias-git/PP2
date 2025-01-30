class Shape:
    def __init__(self):
        self.area_value = 0

    def area(self):
        return self.area_value

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2

sq = Square(5)
print(sq.area())     # output 25