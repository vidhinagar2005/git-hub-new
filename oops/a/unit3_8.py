class emp:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def display(self):
        print("name = ",self.name)
        print("id = ",self.id)
        print("salary = ",self.salary)
    
class myclass:
    @staticmethod
    def mymethod(e):
        e.salary += 1000
        e.display()

v = emp("vid",1,9000)
myclass.mymethod(v)