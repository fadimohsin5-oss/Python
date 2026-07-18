class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width

newRectangle = Rectangle(12,10)
print("area of Rectangle:", newRectangle.area())

class Fruit:
    def __init__(self, f, t):
        self.flavour = f
        self.texture = t

    def info(self):
     print (self.flavour,self.texture)
newFruit = Fruit("sweet", "hard")
newFruit.info()