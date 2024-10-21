def test(num):
    if num > 1:
        for i in range(2, num):
            if num %i ==0:
                print(num,"is not prime number")

            else:
                print(num,"is  prime number")
                break

num = int(input("enter any number = "))
test(num)
            