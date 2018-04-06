import math

class Circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return math.pi*(self.radius**2)

c = Circle(5)

print(c)
print(c.area())
