f1 = open("myfile.txt","w")
i = True

while i == True:
    name = input("enter name = ")
    if name == "ankit":
        i = False

    else:
        f1.write(name)
        f1.write("\n")
