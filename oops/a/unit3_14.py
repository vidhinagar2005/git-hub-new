class A(object):
    def method(self):
        print("A class")
        super().method()

class B(object):
    def method(self):
        print("B class")
        super().method()

class C(object):
    def method(self):
        print("C class")
        super().method()

class X(A, B):
    def method(self):
        print(" X class")
        super().method()

class Y(B, C):
    def method(self):
        print(" Y class")
        super().method()

class P(X, Y, C):
    def method(self):
        print(" P class")
        super().method()

ans = P()
print(P.mro())
ans.method()