class Hexagon():
    def __init__(self,s):
        self.side = s

    def calculate_perimeter(self):
        return self.side*6

h = Hexagon(2)

print(h)
print(h.calculate_perimeter())
