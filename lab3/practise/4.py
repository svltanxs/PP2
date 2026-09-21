import math
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def show(self):
        print(f"({self.x} , {self.y})")
    def move(self,dx , dy):
        self.x = self.x + dx
        self.y = self.y + dy
    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
p1 = Point(0 , 0)
p2 = Point(3 , 4)

p1.show()
p2.show()

p1.move(1 , 1)
p1.show()

print(p1.dist(p2))
