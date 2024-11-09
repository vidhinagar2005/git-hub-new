a = int(input("Enter a = "))
b = int(input("Enter b = "))

try:
    ans = a/b
except ZeroDivisionError:
    print("Error!")

else:
    print("Ans = ",ans)