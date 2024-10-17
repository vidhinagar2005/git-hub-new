class cons:
    def __init__(self,name,age):
        self.name =name
        self.age =age

    def display(self):
        print(self.name +" "+ self.age)

c = cons("vidhi","19")
print(c.display())