import math
class square:
    def area(self, x):
        print("Area = ",(x*x))

class circle(square):
    def area(self, x):
        print("area of circle = %.2f"%(math.pi*x*x))

c1 = circle()
c1.area(4)