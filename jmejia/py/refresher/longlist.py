import time

# This is a mergesort...turns out mergesort is easier to remember than quicksort, and the slice syntax makes it a lot easier.
# This will output the sorted listed -- it will not sort the list in place.
def sortList(list) :
   if len(list) <= 1 :   # both [] and [x] are perfectly sorted -- no work needed
      return list
   else :
      mid = len(list) // 2   # find the midpoint
      a = list[:mid]         # and split the list
      b = list[mid:]         # into two halves
      a = sortList(a)        # sort the first half (recursive call!)
      b = sortList(b)        # so, we keep sorting smaller lists until we get to lists of length 1
      out = []
      while (len(a) > 0) and (len(b) > 0) :   # keep going until one of the two sorted halves has been exhausted...
         if a[0] <= b[0] :        # find which half has the next smallest value
            out.append(a.pop(0))  # and stick that onto the final list we're building
         else :
            out.append(b.pop(0))
      return out + a + b   # ...at which point, one list is empty (concat has no effect) and the other is all larger values, in order -- no need to check which is empty!


# This sieve function has a few optimizations, though I tried to stop before it felt like I was prepping the answer too much.
# The most important optimization is stopping the sieve at the square root of the upper bound.  It's fairly easy to show that by this point, you have found all primes in the range.
# Even for n=100, this speeds up the sieve by TEN TIMES.  For n=1 million, it's A THOUSAND TIMES faster.  This works regardless of the implementation.
# (Rethinking the above...it only speeds up by 10x for a very naive implementation of a sieve.  Compared to an relatively efficient algorithm, it's still  at least 2x as fast.)
# (This is because there are fewer values to check with each new value.)
# Instead of an n-length array of Boolean values, I created a list of values, and iteratively deleted the ones that were multiples.  I don't know how much time this saves.
# It should reducate the memory footprint as the algorithm runs, and at the end, it's very simple to pass out the list of primes without needing another pass.
# Because items are removed, you a) don't need to search for the next prime ahead of you on the next iteration, and b) you skip redundant comparisons for values that have already been eliminated.
# But, I also don't know how slow deleting list elements is.  I do think it saves some time, overall, but I'd need to write another function to compare.
# UPDATE: Well, whatever is going on, this is definitely way slower than using a list of Booleans once you get to larger values of n (start seeing it around 1e5; very obvious at 1e6).
# I didn't even try to only use odd numbers...  Could be optimized further?
# Another cheap optimimzation is only creating a heap of odd numbers -- this is easily done in one step with the range() function.
# This could be simulated with an array of Booleans by only making a list half as long, as long as you remember to include 2 as a prime at the end.
def sieve(n) :
   if n < 2 :
      return []   # edge case covers no primes
   elif n == 2 :
      return [2]   # we can save some time later on by treating this as an edge case
   elif n < 5 :
      return [2,3]   # we can save a little time later on by getting this out of the way, too

   primes = [2,3,5]   # beyond the edge cases of 0-2 primes, always start with 2, 3, and 5 as the first primes

   limit = int(n ** 0.5)   # there is no need to sieve by primes greater than the square root of n (all composites below n will be the product of lesser primes until the greatest prime squared)
   heap = [*range(7,n+1,2)]   # create the heap to sieve -- we save time and memory by only including odd numbers, since all evens > 2 are composite -- we start at 7, since we already have 2/3/5

   for i in reversed(range(1, len(heap), 3)) :   # count every third index in heap and delete them in reverse order, so the index doesn't change -- these are ALWAYS odd multiples of 3
      del heap[i]                                # this is the last regular interval we can rely on -- patterns going forward are more complicated and continue to have diminishing returns

   while primes[-1] <= limit :   # primes[-1] is the next prime to check -- adding next prime before the loop and checking <= often saves an iteration compared to adding after the loop and checking <
      for i,v in enumerate(heap) :   # we need to test the value, but delete by index, so we use enumerate() to get both
         if (v % primes[-1]) == 0 :   # v % primes[-1] is 0 when the value we're testing is divisble by the current prime
            del heap[i]
      primes.append(heap.pop(0))   # the first element left in the heap will always be the next largest prime (and heap[0] will ALWAYS exist, since we stop before limit)
   primes += heap   # at end of while loop ALL remaining values of heap are guranteed to be prime -- we can just tack them on the end
   return primes


def sieve2(n) :
   if n < 2 :
      return []
   out = []
   heap = [True]*(n+1)
   heap[0] = heap[1] = False
   limit = int(n ** 0.5)
   head = seek = 2
   while head <= limit :
      #print("DEBUG: checking prime=" + head)
      out.append(head)
      seek += head
      while seek < len(heap) :
         #print("DEBUG: removing composite=" + seek)
         heap[seek] = False
         seek += head
      seek = head + 1
      while seek < len(heap) :
         #print("DEBUG: looking for next prime=? " + seek)
         if heap[seek] :
            #print("DEBUG: found next prime=" + seek)
            head = seek
            break
         seek += 1
   while seek < len(heap) :
      #print("DEBUG: Done.  Collecting remaining primes...")
      if heap[seek] :
         #print("DEBUG: found next prime=" + seek)
         out.append(seek)
      seek += 1
   return out




def sieve3(n) :
   if n < 2 :
      return []
   out = [2]
   heap = [True]*((n+1)//2)
   heap[0] = False
   limit = int(n ** 0.5)//2
   head = seek = 1
   while head <= limit :
      hval = (2*head)+1
      #print("DEBUG: checking prime=" + str((2*head)+1))
      out.append(hval)
      seek += hval
      while seek < len(heap) :
         #print("DEBUG: removing composite=" + str((2*seek)+1))
         heap[seek] = False
         seek += hval
      head = seek = head + 1
      while seek < len(heap) :
         #print("DEBUG: looking for next prime=? " + str((2*seek)+1))
         if heap[seek] :
            #print("DEBUG: found next prime=" + str((2*seek)+1))
            head = seek
            break
         seek += 1
   while seek < len(heap) :
      #print("DEBUG: Done.  Collecting remaining primes...")
      if heap[seek] :
         #print("DEBUG: found next prime=" + str((2*seek)+1))
         out.append((2*seek)+1)
      seek += 1
   return out




for i in range(10) :
   print(sieve3(i+1))
print()

a = [1,2,3]
b = [7,6,5]
c = []
d = [10]
e = [5,-1,6,2,10,2,0,2,-10]


print(sortList(c))
print(sortList(d))
print(sortList([0,1]))
print(sortList(a))
print(sortList(b))
print(sortList(e))
print()


print("SIEVE:")
for i in range(10) :
   print("Primes up to " + str(i+20) + ": " + str(sieve(i+20)))
print("Primes up to 100: " + str(sieve(100)))
print("Primes up to 100: " + str(sieve2(100)))

print()
print()
print("# of primes up to 1e3: " + str(len(sieve(1000))))
print("# of primes up to 1e4: " + str(len(sieve(10000))))
print("# of primes up to 1e5: " + str(len(sieve(100000))))

time1 = time.time()
sieve(100000)
time2 = time.time()
print("primes up to 1e5 found in: " + str(time2-time1) + " secs")

time1 = time.time()
sieve2(100000)
time2 = time.time()
print("primes up to 1e5 found in: " + str(time2-time1) + " secs")

time1 = time.time()
sieve3(100000)
time2 = time.time()
print("primes up to 1e5 found in: " + str(time2-time1) + " secs")
