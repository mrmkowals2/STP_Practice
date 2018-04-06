class Rectangle():
    def __init__(self, s1, s2):
        self.side1 = s1
        self.side2 = s2

    def calculate_perimeter(self):
        return (self.side1*2) + (self.side2*2)

class Square():
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return (self.side*4)

r = Rectangle(3,4)
s = Square(2)

print(r)
print(s)

print(r.calculate_perimeter())
print(s.calculate_perimeter())
