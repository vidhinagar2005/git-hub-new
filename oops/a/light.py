class traficlight:
    def __init__(self, color):
        self.color = color

    def action(self):
        if self.color == "red":
            self.next_color = "yellow"
            print("stop and wait")

        elif self.color == "yellow":
            self.next_color = "green"
            print("prepare and stop")

        elif self.color == "green":
            self.next_color = "red"
            print("go")
        else:
            self.next_color = "orange"
            print("stop")

for i in ["red","yello","green"]:
    t1 = traficlight(i)
    print(t1.color)
    t1.action()
    print(t1.next_color)
    print("\n")
    