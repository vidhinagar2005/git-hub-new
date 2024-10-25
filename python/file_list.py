list = [1,2,11,28,29,50]
f1 = open("number.txt","w")
f2 = open("prime.txt","w")
for i in list:
    
    f1.write("\n")
    if i % 2 == 0:
        # f1.write(str(i))
        # f2.write(str(i))
        f1.write("Not prime number...")
        f1.write("\n")

    else:
        f2.write(str(i))
        f2.write("prime number...")
        f2.write("\n")