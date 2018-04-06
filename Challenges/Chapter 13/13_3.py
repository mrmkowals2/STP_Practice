class Shape():
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, s1, s2):
        self.side1 = s1
        self.side2 = s2

    def calculate_perimeter(self):
        return (self.side1*2) + (self.side2*2)

class Square(Shape):
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return (self.side*4)

    def change_size(self, i):
        self.side = self.side + i

r = Rectangle(3,4)
s = Square(2)

r.what_am_i()
s.what_am_i()

