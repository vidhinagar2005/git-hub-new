a = 0
b = 1
print(a, b)
num = int(input("Enter number = "))
for i in range(2,num):
    tmp = a + b
    print(tmp,end=" ")
    a = b
    b = tmp
    