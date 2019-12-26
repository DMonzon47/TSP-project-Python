'''Exercise Question 1: Given a two list. Create a third list by picking 
an odd-index element from the first list and even index elements from second.
For Example:

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
'''
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

for i in listOne: 
    print(i)

for i in listOne: 
    print([i])

print(listOne[1])


lst = []

lst.append(('London','UK', 15,14.357))
print(lst)
print(lst[0][1])

#listThree = [(i,i) for i in (listOne, listTwo) if ([i]%2!= 0, [i]%2==0)]

#for i in listOne: 
#   if [i]%2 != 0:
