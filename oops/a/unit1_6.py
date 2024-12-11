a = 20
b = 20

if a is b:
    print("both same")

else:
    print("not same")

if id(a) == id(b):
    print("same")
else:
    print("not same")