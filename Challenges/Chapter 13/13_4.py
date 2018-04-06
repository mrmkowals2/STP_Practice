class Rider():
    def __init__(self, s, h, w):
        self.sex = s
        self.height = h
        self.weight = w

class Horse():
    def __init__(self, s, w, a, r):
        self.sex = s
        self.weight = w
        self.age = a
        self.rider = r

stan = Rider('M',182,90)
h = Horse('M',800,8,stan)

print(h.rider.sex)
print(h.rider.height)
print(h.rider.weight)
