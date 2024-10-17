class student:
    def __init__(self, n, a):
        self.name = n
        self.age = a

#instance method
    def display(self):
        print("name:",self.name)
        print("age:",self.age)

#create object
stud = student("vidhi",19)
stud.display()