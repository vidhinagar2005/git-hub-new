choice = 1
val =0
while choice == 1:
    user = int(input("press 1 for girl's cloth \nprsee 2 for boy's cloth"))
    if user == 1:
        print("welcome to girl section...!")
        amount = int(input("enter your amount = "))
        val += amount
    else:
        print("welcome to boy section...!")

    print("Do u want to again buy any clothes then press 1...")
    choice = int(input("enter your choice = "))

print("total is = ",val)