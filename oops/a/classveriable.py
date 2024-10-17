class student:
    name = "vidhi"
    age = 19
    @classmethod
    def modify(stud):
        stud.name = "vidhi nagar"

#create object
s1 = student()
print("name:",s1.name)
print("age:",s1.age)

s1.modify()
print("name:",s1.name)
print("age:",s1.age)
