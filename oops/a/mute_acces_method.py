class player:
    #mutetor method
    def setname(self, name):
        self.name = name
    #accesor method
    def getname(self):
        return self.name
    #mutetor method
    def setruns(self, runs):
        self.runs = runs
    #accesor method
    def getruns(self):
        return self.runs
    
n = int(input("How many players..?"))
i = 0
while i<n:
    p = player()
    name = input("Enter name = ")
    p.setname(name)
    runs = int(input("Enter runs = "))
    p.setruns(runs)
    print("Hello",p.getname())
    print("your score is = ",p.getruns())
    i += 1
    print("--------------------------------")

print("Game over....")