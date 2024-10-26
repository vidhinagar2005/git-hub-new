evn = 0
for i in range(1,10):
    if i % 2 == 0:
        print(i,"Even number")
        evn += i
    else:
        print(i,"odd number")
print("total = ",evn)
