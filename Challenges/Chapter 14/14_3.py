class Square():
    squares = []

    def __init__(self, side):
        self.s = side
        self.squares.append(self.s)

    def print_size(self):
        print("{} by {} by {} by {}".format(self.s, self.s, self.s, self.s))

def same_object(square_1,square_2):
    print(square_1 is square_2)

s1 = Square(4)
s2 = Square(6)

same_object(s1,s2)
