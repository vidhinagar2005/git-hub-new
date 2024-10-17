class student:
    def __init__(self):
        self.name = "vidhi"
        self.age = 19
        self.marks = 79
    #instance method
    def display(self):
        print("Name = ",self.name)
        print("Age  = ",self.age)
        print("Marks = ",self.marks)

s = student()
s.display()