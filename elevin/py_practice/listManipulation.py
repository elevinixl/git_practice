def remove1(n, element):
    for index in range(len(n)-1,-1,-1):
        if n[index] == element:
            n.pop(index)
    return n

def remove2(n, element):
    newList = []
    for value in n:
        if value != element:
            newList.append(value)
    return newList

def addElement(n,element):
    return n + [element]

def insertConcat(theList, index, element):
    if index >= len(theList):
        return 'Error'
    return theList[:index] + [element] + theList[index:]

print(remove1([3,4,5,2,3,1], 3))
print(remove2([3,4,5,2,3,1], 3))
print(addElement([3,2],1))
print(insertConcat([1,2,3,4,5],3,100))