list = [1,2,11,28,29,50]
f1 = open("number.txt","w")
for i in list:
    f1.write(str(i))
    f1.write("\n")