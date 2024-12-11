def search(list,n):
    for i in range(len(list)):
        if list[i] == n:
            return True
            return False
      
list = [1,3,"vidhi",5,"nagar"]
n="vidhi" 
if search(list,n):
    print("found")
else:
    print("not found")


