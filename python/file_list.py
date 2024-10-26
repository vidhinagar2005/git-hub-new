list = [1,2,3,4,5,6,7,8,9,10]
f1 = open("data.txt","w")
for i in list:
    f1.write(str(i))
    f1.write("\n")

f1.close()

f2 = open("data.txt","r")

for k in f2:
    f2.readlines()
    f3 = open("num.txt","a")
    
    f3.write(k)


    

