
#stack is for last in first output (lifo)
books = []
print(books)

books.append('c')
print(books)

books.append('python')
print(books)


books.pop(0)
print(books)

#queue is for first in first output (fifo)
ticket = []

ticket.append('aynul')
print('aynul ticket name :', ticket)


ticket.append('avee')
print ('aynul and avees ticket name  are :', ticket)


#pop in queue

ticket.pop(0)
print('after pop, now serial is ticket for', ticket)



# linear search in python3
lineer = [2,3,4,5,6,8]
for i in lineer:
    if i == 3:
        print('found: ', lineer.index(3)) 


#duplicate value remove in python3

array = [3,4,5,4,5,3,4,5,3,4,2,2,4,5]

setArray = set(array)
listSetArray = list(set(array))

print('without duplicate value of this list mis: ', listSetArray)


removeDuplicate = []

for duplicate in array:
    if duplicate not in removeDuplicate:
        removeDuplicate.append(duplicate)

print('without duplicate array value are', removeDuplicate)
sortDuplicate = sorted(removeDuplicate)
print(sortDuplicate)

for i in sortDuplicate:
    print(i)
    newI = []
    newI.append(i)
    print(newI)

    
