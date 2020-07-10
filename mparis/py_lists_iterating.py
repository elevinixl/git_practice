ex=[1,2,3,4,5,6]
ex2=[1,2,3,4,5,6]
ex3=['kirk', 'spock', 'bones', 'uhura', 'uhura', 'chekov', 'chapel','sulu']
ex4=[i * 3 for i in ex]
ex5= [[1,2,3],[4,5,6],[7,8,9]]


#1
def listResult(ex):
    return sum(ex)
print('Sum of list elements: '+str(listResult(ex)))

#2
def listResult(ex):
    ex.sort()
    return(ex[-1])
print('Largest number in list: '+str(listResult(ex)))

#3
def listResult(ex):
    for i in ex:
        ex.append(i*3)
        print(ex4)
print('All list elements multiplied by 3: ' + str(ex4))

#4
def listResult(ex2):
    if ex==ex2:
        return 'Are lists ex & ex2 identical?: True!'
    else:
        return 'Are lists ex & ex2 the identical?: False!'
print(listResult(ex2))

#5a
#def listResult(ex3):
#    for i in enumerate(ex3):


#print(listResult(ex3))

#5b
def listResult(ex3):
    idx = ex3.index('uhura')
    ex3b = (('The first instance of the word...' + ex3[idx]) +' is at index...'+ str(idx)+'')
    return ex3b
print(listResult(ex3))

#6
#def listResult(ex5):
#    print('\n')
 #   for i in enumerate(ex5):

#print(listResult(ex5))




