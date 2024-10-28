list1 = [i for i in range(1, 8)]
print(list1)

#append
list1.append(9)
print(list1)

#insert
list1.insert(2,10)
print(list1)

#copy
list = list1.copy()
print("list",list)

#extend
extra = ['a','b','c']
list.extend(extra)
print(list)

#remove
#compulsory to give element in ()
list.remove('c')
print(list)

#pop
#not give some argument
print(list.pop())
print(list)


#sort
sorting = [3,5,7,1,2,8,3,5,9]
sorting.sort()
print("sorted",sorting)


#reverce
sorting.reverse()
print("reverce",sorting)

#clear
#it clear the list and give empty list...
sorting.clear()
print(sorting)
