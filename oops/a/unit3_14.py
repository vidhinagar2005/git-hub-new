class a:
    def method(self):
        print("A class")
        # super().method()
        

class b:
    def method(self):
        print("B class")
        # super().method()

class c:
    def method(self):
        print(" C class")
        super().method()

class x(a, b):
    def method(self):
        print("class x")
        super().method()
    
class y(b, c):
    def method(self):
        print(" class y")
        super().method()

class p(x, y, c):
    def method(self):
        print("p class")
        super().method()


newp = p()
# newp.method() 
print(p.mro())

newp.method()