
# class variable
# class sample:
#     var = 10

#     @classmethod
#     def modify(cls):
#         cls.var += 1

# s1 = sample()
# print(s1.var)
# s1.modify()
# print(s1.var)

#instance variable
class new:
    def __init__(self):
        self.x = 10

    def display(self):
        self.x +=1

n1 = new()
print(n1.x)
n1.display()
print(n1.x)