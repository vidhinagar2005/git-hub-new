choice = 0
while choice != 3:
    print("1.circle")
    print("2.triangle")
    print("3. exit")
    choice = int(input("enter choice = "))
    if choice == 1:
        pi = 3.14
        radius = float(input("enter radius = "))
        area = pi * radius * radius
        print(area)

    elif choice == 2:
        a = float(input("first side = "))
        b = float(input("second side = "))
        c = float(input("third side = "))
        s = (a + b + c)/2
        area = (s * (s-a)*(s-b)*(s-c)) ** 0.5
        print(area)
    elif choice == 3:
        exit()

    else:
        print("bye bye")
        

