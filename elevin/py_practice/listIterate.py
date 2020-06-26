def listSum(n):
    theSum = 0
    for value in n:
        theSum += value
    return theSum

def listMax(n):
    theMax = -1 * 10 ** 10000
    for value in n:
        if theMax < value:
            theMax = value
    return value

def multByThree(n):
    for index in range(len(n)):
        n[index] = n[index] * 3
    return n

def listFind(theList, element):
    for index, value in enumerate(theList):
        if value == element:
            return index
    return False

def nestedPrint(n):
    outString = ''
    for value1 in n:
        for value2 in value1:
            outString += str(value2) + ' '
    return outString

print(multByThree([1,2,3]))
print(listFind([2,3,4],3))
print(nestedPrint([[1,2],[3,4]]))