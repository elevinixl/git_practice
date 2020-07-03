def lowestNumber(numList) :
   if len(numList) < 1 :
      return None
   else :
      low = numList[0]
      for value in numList :
         if value < low :
            low = value
      return low

print(lowestNumber([]))
print(lowestNumber([1,2,3]))
print(lowestNumber([6,5,4]))
print()


def longestWord(strList) :
   if len(strList) < 1 :
      return None
   else :
      long = strList[0]
      for word in strList :
         if word > long :
            long = word
      return long

print(longestWord([]))
print(longestWord(["a","to","the"]))
print(longestWord(["hungry","hippo","head"]))
print()


def characterSum(strList) :
   if len(strList) < 1 :
      return 0
   else :
      sum = 0
      for word in strList :
         sum += len(word)
      return sum

print(characterSum([]))
print(characterSum(["a","to","the"]))
print(characterSum(["hungry","hippo","head"]))
print()


def largerThan(numList, cutoff) :
   if len(numList) < 1 :
      return []
   else :
      largerList = []
      for value in numList :
         if value > cutoff :
            largerList.append(value)
      return largerList

print(largerThan([],4))
print(largerThan([1,2,3],4))
print(largerThan([6,5,4],4))
print()


def itemCount(anyList, item) :
   if len(anyList) < 1 :
      return 0
   else :
      count = 0
      for value in anyList :
         if value == item :
            count += 1
      return count

print(itemCount([],4))
print(itemCount([1,2,3,2],2))
print(itemCount(["hungry","hippo","head"],"huh?"))
print()


def listPlusPlus(numList) :
   if len(numList) < 1 :
      return []
   else :
      largerList = []
      for value in numList :
         largerList.append(value+1)
      return largerList

print(listPlusPlus([]))
print(listPlusPlus([1,2,3]))
print(listPlusPlus([6,5,4]))
print()
