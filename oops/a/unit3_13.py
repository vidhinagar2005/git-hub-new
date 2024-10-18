class father:
    def height(self):
        print("Height is 6.0 foot")

class mother:
    def age(self):
        print("Age is 30 year")

class child(father, mother):
    def both(self):
        print("child of mother and father")

print("child is inherite")
c1 = child()
c1.height()
c1.age()
c1.both()