def getCSL(aList):
    if len(aList) == 0:
        return ''
    elif len(aList) == 1:
        return str(aList[0])
    elif len(aList) == 2:
        return str(aList[0]) + ' and ' + str(aList[1])
    else:
        output = ''
        for i in aList[:-1]:
            output += str(i) + ', '
        output += 'and ' + aList[-1]
        return output


spam = ['apples', 'bananas', 'tofu', 'cats']

print(getCSL(spam))
