import time

def newSort(theList):
    newList = []
    while len(theList) > 0:
        min = 10000000000000
        for value in theList:
            if value < min:
                min = value
        newList.append(min)
        theList.remove(min)
    return newList

print(newSort([3,1,2,4,5]))

def findPrimes(n):
    # Create prime array
    # Index of array is the number, value indicates if it is prime or not.
    # For instance prime[30] tells us if 30 is prime, so eventually we will want prime[30] = False
    primes = [True]*(n+1)
    # Manually set 0 and 1 to not prime (False)
    primes[0] = False
    primes[1] = False

    for number in range(2,n+1):
        #set any index that is a multiple of number as False in the array
        multiple = number*2
        while multiple <= n:
            primes[multiple] = False
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

def trainNav(train):
    currentLocation = len(train)//2
    while True:
        print('You are in the ' + train[currentLocation][0])
        move = input('Where would you like to go? [f]orwards, [b]ackwards, [j]ump off\n')
        if move == 'j':
            break
        elif move == 'b':
            if currentLocation + 1 < len(train):
                currentLocation += 1
                print(train[currentLocation][1])
            else:
                print('You are already in the last car.')
        elif move == 'f':
            if currentLocation - 1 >= 0:
                currentLocation -= 1
                print(train[currentLocation][1])
            else:
                print('You are already in the first car.')

trainNav([['engine','The engine is hot, help the engineer shovel some coal into the boiler!'],
       ['First class car','Look at all the fancy people!'],
       ['Passenger car','You should find your seat.'],
       ['caboose','Everything is red!']])