import time

def findPrimes(n):
    # Create prime array
    # Index of array is the number, value indicates if it is prime or not.
    # For instance prime[30] tells us if 30 is prime, so eventually we will want prime[30] = False
    primes = [True]*(n+1)
    # Manually set 0 and 1 to not prime (False)
    # FILL IN!

    for number in range(2,n+1):
        #set any index that is a multiple of number as False in the array
        multiple = number*2
        while multiple <= n:
            #FILL IN
            multiple += number

    #Print primes
    outString = 'Prime numbers are: '
    for i, v in enumerate(primes):
        if v:
            outString += str(i)+ ' '
    return outString

time1 = time.time()
print(findPrimes(100))
time2 = time.time()
print('It took: ' + str(time2-time1) + ' secs')