a = eval(input("Enter a = "))
b = input("Enter b = ")

try:
    ans = a/b
except (TypeError, SyntaxError):
    print("Error!")

else:
    print("Ans = ",ans)