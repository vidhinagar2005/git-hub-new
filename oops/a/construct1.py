class student:
    def __init__(self):
        self.name = "vidhi"
        self.age = 19
        self.runs = 20

#instance method
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("runs:",self.runs)

#create object to student class

stud = student()

#call the method
stud.display()
