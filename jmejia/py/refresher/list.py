def listLength(list) :
   return len(list)

def firstElement(list) :
   if listLength(list) == 0 :
      return None
   else :
      return list[0]

def thirdElement(list) :
   if listLength(list) < 3 :
      return None
   else :
      return list[2]

def lastElement(list) :
   if listLength(list) == 0 :
      return None
   else :
      return list[-1]

def lastElement2(list) :
   if listLength(list) == 0 :
      return None
   else :
      return list[listLength(list)-1]



def twoThruFive(list) :
   if listLength(list) < 5 :
      return None
   else :
      return list[1:5]

def oneThruFour(list) :
   if listLength(list) < 4 :
      return None
   else :
      return list[0:4]

def threeThruEnd(list) :
   if listLength(list) < 3 :
      return None
   else :
      return list[2:]



def copyFirst(list) :
   if listLength(list) < 2 :
      return None
   else :
      list[1] = list[0]
      return list



a = [1,2,3,4]
b = []
c = [5]
d = [10,9,8,7,6,5,4,3,2,1]
e = [10,20,30,40,50]


print(listLength(a))
print(listLength(b))
print(listLength(c))
print(listLength(d))
print(listLength(e))
print()
print(firstElement(a))
print(firstElement(b))
print(firstElement(c))
print(firstElement(d))
print(firstElement(e))
print()
print(thirdElement(a))
print(thirdElement(b))
print(thirdElement(c))
print(thirdElement(d))
print(thirdElement(e))
print()
print(lastElement(a))
print(lastElement(b))
print(lastElement(c))
print(lastElement(d))
print(lastElement(e))
print()
print(lastElement2(a))
print(lastElement2(b))
print(lastElement2(c))
print(lastElement2(d))
print(lastElement2(e))
print()
print(twoThruFive(a))
print(twoThruFive(b))
print(twoThruFive(c))
print(twoThruFive(d))
print(twoThruFive(e))
print()
print(oneThruFour(a))
print(oneThruFour(b))
print(oneThruFour(c))
print(oneThruFour(d))
print(oneThruFour(e))
print()
print(threeThruEnd(a))
print(threeThruEnd(b))
print(threeThruEnd(c))
print(threeThruEnd(d))
print(threeThruEnd(e))
print()
print(copyFirst(a))
print(copyFirst(b))
print(copyFirst(c))
print(copyFirst(d))
print(copyFirst(e))

