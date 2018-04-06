class Square():
    squares = []

    def __init__(self, side):
        self.s = side
        self.squares.append(self.s)

s1 = Square(4)
s2 = Square(6)

print(Square.squares)
