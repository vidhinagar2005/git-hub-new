class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name,"\n",self.age)

s1 = student("vidhi",19)
s1.display()
