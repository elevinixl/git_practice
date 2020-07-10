#consider renaming variables in ways that make it clear if its explicitly expecting a number or string

ex=[2,7,-2,3,4,4,5,1,10]
ex2=['Fivee','Four','Sevennn','Tu','Nineeeeee','Short']
ex3=4
#-------------------------------------------------------------------------------------
#1a
def listResult(ex):
    lowest = ex[0]
    for x in ex:
        if x < ex[0]: #Won't yield correct result in some cases
            lowest = x
    return lowest
print('[1-A] Lowest number in list is: '+ str(listResult(ex)))
#1b

def listResult(ex):
    lowest = ex[0]  #Add validation check that list at least has one element
    for x in ex:
        if x < lowest:
            lowest = x
    return lowest
print('[1-B] Lowest number in list is: '+ str(listResult(ex)))

#-------------------------------------------------------------------------------------
#2a
def listResult(ex2): #Incorrect, returns x, which is always last value
    largest = ex2[0]
    for x in ex2:
        if len(x) > len(ex2[0]):
            largest = len(x)
    return x
print(' [2-A] Longest word in list is: '+ str(listResult(ex2)))
#2b
def listResult(ex2): #Correct, returns largest value
    largest = ex2[0]
    for x in ex2:
        if len(x) > len(largest):
            largest = x
    return largest
print(' [2-B] Longest word in list is: '+ str(listResult(ex2)))

#-------------------------------------------------------------------------------------
#3a
def listResult(ex2):
    addnums = 0
    for x in ex2:
        addnums = len(x)+addnums
    return addnums
print('   [3-A] Total number of characters in list: '+ str(listResult(ex2)))

#-------------------------------------------------------------------------------------
#4a
def listResult(ex,ex3):
    result = []
    for x in ex:
        if x > ex3:
            result = result+[x]
    return result
print('    [4-A] Numbers in list that are greater than (4): '+ str(listResult(ex,ex3)))

#-------------------------------------------------------------------------------------
#5a
def listResult(ex,ex3):
    result = []  #count = 0
    for x in ex:
        if x == ex3:
            result = result+[x] #count += 1
    return len(result) #count
print('     [5-A] Number of times (4) displays in list: '+ str(listResult(ex,ex3)))

#-------------------------------------------------------------------------------------
#6a
def listResult(ex):
    result = []
    for x in ex:
        result = result + [x+1]
    return result
print('      [6-A] Each item in list +1: '+ str(listResult(ex)))






