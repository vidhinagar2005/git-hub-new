class a(object):
    def method(self):
        print("A class")
        super().method()

class b(object):
    def method(self):
        print("B class")
        super().method()

class c(object):
    def method(self):
        print("C class")
        super().method()

class x(a, b):
    def method(self):
        print(" X class")
        super().method()

class y(b, c):
    def method(self):
        print(" Y class")
        super().method()

class p(x, y, c):
    def method(self):
        print(" P class")
        super().method()

ans = p()
print(p.mro())
ans.method()