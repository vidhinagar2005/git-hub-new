class teacher:
    def __init__(self, id):
        self.id = 2005

    def display(self):
        print("teacher id = ",self.id)

class student(teacher):
    def __init__(self):
        self.id = 2024

    def display(self):
        print("student id = ",self.id)

s1 = student()
s1.display()