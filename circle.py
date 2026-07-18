class Circle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width

newCircle = Circle(12,10)
print("area of Circle:", newCircle.area())
