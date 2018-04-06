class Square():
    squares = []

    def __init__(self, side):
        self.s = side
        self.squares.append(self.s)

    def print_size(self):
        print("{} by {} by {} by {}".format(self.s, self.s, self.s, self.s))

s1 = Square(4)
s2 = Square(6)

print(s1.print_size())
