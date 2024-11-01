class square:
    def __init__(self,x):
        self.x = x

    def area(self):
        print("Area of square = ",self.x * self.x)

class rectangle(square):
    def __init__(self,a,b):
        super().__init__(a)
        self.b = b

    def area(self):
        super().area()
        print("Area of rectangle = ",self.x * self.b)

v = int(input("length = "))
i = int(input("Breath = "))
r = rectangle(v,i)
r.area()