def exclude(l, a) :
   out = []
   for v in l :
      if v != a :
         out.append(v)
   return out

def totallyNotAppend(l,a) :
   l += [a]
   return None

def totallyNotInsert(l,i,a) :  
   if i < 0 :   # Get those negative indices outta here.  (Actually...Python might handle those fine.  Does insert() take negative indices?)
      return "ERROR"
   elif i == 0 :   # Insert at the beginning.
      l[:] = [a] + l   # l[:] is an easy way to overwrite the whole list without changing the reference (passed in list parameter is permanently updated)
      return None
   elif i == len(l) :   # Insert at the end.
      l[:] += [a]
      return None
   elif i > len(l) :   # Check whether index is too far past the end of the list.
      return "ERROR"
   else :
      s = l[:i]            # Since working with slices more...
      e = l[i:]            # It's possible this code alone would work find for one or both of the other edge cases.
      l[:] = s + [a] + e   # I have not tested this, though.
      return None

a = [1,2,3]
b = []

print(exclude(a,2))
print(exclude(a,4))
print(exclude(b,2))
print()
print(a)
print(totallyNotAppend(a,4))
print(a)
print()
print()
print(a)
print(totallyNotInsert(a,2,"middle"))
print(a)
totallyNotInsert(a,5,"end")
print(a)
totallyNotInsert(a,0,"beginning")
print(a)
print(b)
totallyNotInsert(b,1,"NOPE")
print(b)
totallyNotInsert(b,0,"first")
print(b)
totallyNotInsert(b,-1,"NOPE")
print(b)

