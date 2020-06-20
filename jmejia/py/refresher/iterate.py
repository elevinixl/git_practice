import copy

def sum(list) :
   if len(list) == 0 :
      return 0
   else :
      x = 0
      for v in list :
         x += v
      return x

def max(list) :
   if len(list) == 0 :
      return None
   else :
      x = list[0]
      for v in list :
         if x < v :
            x = v
      return x

def triple(list) :
   trip = copy.deepcopy(list)
   for i,v in enumerate(trip) :
      trip[i] = 3*v
   return trip

def compare(a, b) :
   if len(a) != len(b) :
      return False
   for i in range(len(a)) :
      if a[i] != b[i] :
         return False
   return True

def find(list, val) :
   if len(list) == 0 :
      return False
   for i,v in enumerate(list) :
      if v == val :
         return i
   return False

def find2(list, val) :
   if len(list) == 0 :
      return False
   for i in range(len(list)) :
      if list[i] == val :
         return i
   return False

def flatten(mat) :
   for l in mat :
      if type(l) is list :   # Extra check that let's us print lists that contain a mix of lists and non-lists.
         for v in l :
            print(str(v) + ' ',end='')
      else :
         print(str(l) + ' ',end='')
   print()

a = [1,2,3]
b = []
c = [1,-2]
d = [[1,2],[3,4]]
e = [[5,6],7]

print(sum(a))
print(sum(b))
print(sum(c))
print()
print(max(a))
print(max(b))
print(max(c))
print()
print(triple(a))
print(triple(b))
print(triple(c))
print()
print(compare(a,a))
print(compare(a,triple(a)))
print(compare(a,b))
print(compare(a,c))
print()
print(find(a,2))
print(find2(a,2))
print(find(b,2))
print(find2(b,2))
print(find(c,2))
print(find2(c,2))
print()
flatten(a)
flatten(b)
flatten(d)
flatten(e)
