class add:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def avg(self):
        return(self.a + self.b) / 2
    
s1 = add(10,20)
print("a=", s1.a, "b=", s1.b)
print("avereage = ", s1.avg())