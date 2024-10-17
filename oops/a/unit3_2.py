class student:
    def __init__(self, name="mittu", age=20, marks=34):#default values are given
        self.name = name
        self.age = age
        self.marks = marks
    #instance method
    def display(self):
        print("Name = ",self.name)
        print("Age =",self.age)
        print("Marks = ",self.marks)
s = student("vidhi",19,23)
s.display()