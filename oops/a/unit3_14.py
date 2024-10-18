class a:
    def method(self):
        print("A class")
        super().method()
        

class b:
    def method(self):
        print("B class")
        super().method()

class c:
    def method(self):
        print(" C class")
        super().method()

class x(a, b):
    def method(self):
        print("class add a and b")
        super().method()
    
class y(b, c):
    def method(self):
        print(" add class b and c")
        super().method()

class p(x, y, c):
    def method(self):
        print("p class")
        super().method()


newp = p()
newp.method() 