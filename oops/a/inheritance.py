class car:
    @staticmethod
    def print():
        print("hello my name is vidhi...")
        name = "vidhi"

class toyota(car):
    def display(self, type):
        toyota.type = type

t1 = toyota()
# print(t1.name)
# print(t1.type)
print(t1.display("abc"))
print(t1.print())