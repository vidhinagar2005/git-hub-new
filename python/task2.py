a = 0
b = 1
ans = 0
print("a = ",a,"b = ",b)
num = int(input("Enter the number = "))
new = num
while num > 0:
    r = num%10
    
    ans += r ** 3
    print(ans)
    num = num //10

if ans == new:
    print("armstrong")

else:
    print("not armstrong")

