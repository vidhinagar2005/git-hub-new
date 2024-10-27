amount = int(input("Enter any amount = "))
rate = float(input("Enter the rate of amount = "))
year = int(input("Enter the year = "))
num = 1

while num<=year:
    a = amount * rate / 100
    print("year =",year,"interest = ",a,"total = ",amount + a)
    num += 1
    amount += a
    
    