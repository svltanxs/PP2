class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,lenght):
        self.lenght = lenght
    def area(self):
        return self.lenght ** 2
p1 = Shape()
print(p1.area())

p2 = Square(4)
print(p2.area())