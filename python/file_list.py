list = [1,2,3,4,5,6,7,8,9,10]
# f1 = open("data.txt","w")
# for i in list:
#     f1.write(str(i))
#     f1.write("\n")

# f1.close()

f2 = open("data.txt","r")
msg = f2.readlines()
f3 = open("num.txt","a")
main = f3.write(str(msg))

for k in main:
    if k % 2 == 0:
        
        f3.write(str("divide"))

    

