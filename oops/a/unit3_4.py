class student:
    #mutator
    def setname(self, name):
        self.name = name

    #accesor 
    def getname(self):
        return self.name
    
    #mutator
    def setage(self, age):
        self.age = age

    #accessor
    def getage(self):
        return self.age
    
n = int(input("How amny studenets = "))
i = 0
while i<n:
    s = student()
    name = input("Enter name = ")
    s.setname(name)
    age = int(input("enter age = "))
    s.setage(age)
    print("Hii..",s.getname())
    print("Your age is..",s.getage())
    i+=1
    print("------------------------------")