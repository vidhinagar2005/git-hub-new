class teacher:
    def __init__(self):
        self.id = 1001

    def display(self):
        print("id id",self.id)

class student:
    def __init__(self):
        self.id = 1
    def display(self):
        print("id is=",self.id)

s = student()
s.display()
s1 = teacher()
s1.display()