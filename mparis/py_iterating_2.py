ex=[2,5,3,4,4,7,1,10]
ex2=['Fivee','Four','Sevennn','Tu','Nineeeeee']
ex3=4
#-------------------------------------------------------------------------------------
#1a
def listResult(ex):
    lowest = ex[0]
    for x in ex:
        if x < ex[0]:
            lowest = x
    return lowest
print('[1-A] Lowest number in list is: '+ str(listResult(ex)))
#1b
def listResult(ex):
    lowest = 999999
    for x in ex:
        if x < lowest:
            lowest = x
    return lowest
print('[1-B] Lowest number in list is: '+ str(listResult(ex)))

#-------------------------------------------------------------------------------------
#2a
def listResult(ex2):
    largest = ex[0]
    for x in ex2:
        if len(x) > ex[0]:
            largest = len(x)
    return x
print(' [2-A] Longest word in list is: '+ str(listResult(ex2)))
#2b
def listResult(ex2):
    largest = len(ex2[0])
    for x in ex2:
        if len(x) > largest:
            largest = len(x)
    return x
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
    result = []
    for x in ex:
        if x == ex3:
            result = result+[x]
    return len(result)
print('     [5-A] Number of times (4) displays in list: '+ str(listResult(ex,ex3)))

#-------------------------------------------------------------------------------------
#6a
def listResult(ex):
    result = []
    for x in ex:
        if x > -999999:
            result = result + [x+1]
    return result
print('      [6-A] Each item in list +1: '+ str(listResult(ex)))





