class mother:
    def height(self):
        print("Height = 6 foot ")

class father:
    def color(self):
        print("color fair")

class child(mother,father):
    pass

c1 = child()
c1.height()
c1.color()