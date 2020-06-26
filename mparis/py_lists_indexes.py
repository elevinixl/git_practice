ex=[1,2,3,4,5,6]
#1
def listResult(ex):
    return len(ex)
print('List length: '+str(listResult(ex)))

#2
def listResult(ex):
    if len(ex)==ex[-1]:
        return ex[0]
    else:
        print('Invalid!')
print('1st list element, validated: '+str(listResult(ex)))

#3
def listResult(ex):
    return ex[2]
print('3rd list element: '+str(listResult(ex)))

#4a
def listResult(ex):
    return ex[-1]
print('Last list element, negative index: '+str(listResult(ex)))
#4b
def listResult(ex):
    var1= len(ex)-1
    return ex[var1]
print('Last list element, positive index: '+str(listResult(ex)))

#5
def listResult(ex):
    return ex[1:5]
print('2nd through 5th elements: '+str(listResult(ex)))

#6
def listResult(ex):
    return ex[0:4]
print('1st through 4th elements: '+str(listResult(ex)))

#7
def listResult(ex):
    return ex[2:]
print('3nd through remainder of elements: '+str(listResult(ex)))

#8
def listResult(ex):
    ex[1]=ex[0]
    return ex[:4]
print('2nd element replaced by first element: '+str(listResult(ex)))
