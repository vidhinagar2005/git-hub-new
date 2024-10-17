class bank:
    def __init__(self, name , balance =0.00):
        self.name = name
        self.balance = balance

    def deposite(self, amount):
        self.balance +=amount
        return self.balance
    
    def withdrow(self, amount):
        if amount > self.balance:
            print("Low balace...")
        else:
            self.balance -= amount
            return self.balance
    

name = input("Enter your name = ")
balance = int(input("enter your balance = "))
b = bank(name, balance)
while(True):
    print("1. for deposite\n2. for withdraw\n3. for exit")
    choice = int(input("Enter your choice = "))
    if choice == 1:
        dept = int(input("Enter your dept amount = "))
        print("balace of deposite=",b.deposite(dept))

    elif choice == 2:
        withd = int(input("Enter withdraw amount = "))
        print("balace of withdreaw = ",b.withdrow(withd))

    elif choice == 3:
        print("account going to exit state...")
        exit()


