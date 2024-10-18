class sum:
    def add(self, a = None, b = None, c = None):
        if a!= None and b!= None and c!= None:
            print("sum of three number = ",(a+b+c))

        elif a!= None and b!=None:
            print("sum of two number = ",(a+b))

        else:
            print("please enter two or three argumenrs")

c1 = sum()
c1.add(11,22,33)
c1.add(10)
c1.add(11,22)