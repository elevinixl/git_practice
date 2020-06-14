Ex=[1,2,3,4,5,6]
#1
def listLength(Ex):
    return len(Ex)
print('List Length: '+str(listLength(Ex)))

#2
def listLength(Ex):
    if len(Ex)==Ex[-1]:
        return Ex[0]
    else:
        print('Invalid!')
print('1st list element, validated: '+str(listLength(Ex)))

#3
def listLength(Ex):
    return Ex[2]
print('3rd list element: '+str(listLength(Ex)))

#4
def listLength(Ex):
    return Ex[-1]
print('Last list element, negative index: '+str(listLength(Ex)))

def listLength(Ex):
    return Ex[5:]
print('Last list element, positive Index: '+str(listLength(Ex)))

#5
def listLength(Ex):
    return Ex[1:5]
print('2nd through 5th elements: '+str(listLength(Ex)))

#6
def listLength(Ex):
    return Ex[0:4]
print('1st through 4th elements: '+str(listLength(Ex)))

#7
def listLength(Ex):
    return Ex[2:]
print('3nd through remainder of elements: '+str(listLength(Ex)))

#8
def listLength(Ex):
    Ex[1]=Ex[0]
    return Ex[:4]
print('2nd element replaced by first element: '+str(listLength(Ex)))
