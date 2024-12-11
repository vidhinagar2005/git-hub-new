mini = int(input("minimum = "))
maxi = int(input("maximum = "))
even = 0
odd = 0

for i in range(mini, maxi + 1):
    if i %2 == 0:
        even+=i
    else:
        odd+=i
print(even,odd)