number = [1,2,3,4,5]

square = list(map(lambda x: x * x,number))
print("square",square)

#filter
number = [1,4,5,3,4,2,10]
even = list(filter(lambda x:x % 2 ==0,number))
print(even)


#lamda with sorted
data = [("vidhi",20), ("mittu",1), ("lalit",30)]
sort = sorted(data, key=lambda x:x)
print(sort)
