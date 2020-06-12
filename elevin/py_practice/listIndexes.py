def listLength(n):
    return len(n)

def firstElement(n):
    if len(n) >= 1:
        return n[0]
    else:
        return 'List not long enough'

def firstElement2(n):
    return n[0] if len(n) >= 1 else 'List not long enough'

def thirdElement(n):
    if len(n) >= 3:
        return n[2]
    else:
        return 'List not long enough'

def lastElement(n):
    if len(n) >= 1:
        return n[-1]
    else:
        return 'List not long enough'

def lastElement2(n):
    if len(n) >= 1:
        return n[len(n)-1]
    else:
        return 'List not long enough'

def secondFifth(n):
    if len(n) >= 5:
        return n[1:5]
    else:
        return 'List not long enough'

def firstFourth(n):
    if len(n) >= 4:
        return n[:4]
    else:
        return 'List not long enough'

def thirdEnd(n):
    if len(n) >= 3:
        return n[2:]
    else:
        return 'List not long enough'

def replaceSecond(n):
    if len(n) >= 2:
        n[1] = n[0]
        return n
    else:
        return 'List not long enough'

print(listLength([3,4]))
print(firstElement([2,3,4]))
print(firstElement2([2,3,4]))
print(lastElement2([5,4,3,2,1]))
print(secondFifth([1,2,3,4,5,6]))
print(replaceSecond([1,2,3,4]))
