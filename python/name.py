name2 = input("Enter your file name = ")

f1 = open(name2+".txt","w")

for i in range(0,5):
    custom = input("Enter your name = ")
    f1.write(custom)
    f1.write("\n")

f1 =open(name2+".txt","r")
print(f1.read())

