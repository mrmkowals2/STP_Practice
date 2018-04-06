class Apple():
    def __init__(self, c, w, s, t):
        self.colour = c
        self.weight = w
        self.size = s
        self.taste = t

a = Apple('red',120,'large',7.5)

print(a)
print("Colour = "+str(a.colour))
print("Weight = "+str(a.weight))
print("Size = "+str(a.size))
print("Taste out of 10 = "+str(a.taste))
