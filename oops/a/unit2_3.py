list = [1,2,3,4,5,4,4,4,4]
print(list)

#append
list.append(6)
print(list)

#insert
list.insert(1,98)
print(list)

#remove
list.remove(6)
print(list)

#pop
list.pop() #last element remove
print(list)

#pring using index
print(list.index(2))

#count element
print(list.count(4))


# import array as np
# arr = np.array([1,2,3,4,5])
# print(arr.tolist())