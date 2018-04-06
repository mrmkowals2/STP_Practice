class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return self.base*self.height/2

t = Triangle(3,4)

print(t)
print(t.area())
