class dog:
    def bark(self):
        print("Bow Wow")

class duck:
    def talk(self):
        print("Quake Quake")

class human:
    def talk(self):
        print("Hello")

def call_back(obj):
    if hasattr(obj,"talk"):
        obj.talk()
    elif hasattr(obj, "bark"):
        obj.bark()

    else:
        print("Wrong object")


x = duck()
call_back(x)
x = human()
call_back(x)
x = dog()
call_back(x)