def commaCode(n):
    out = ''
    for index, value in enumerate(n):
        if index == 0:
            out += value
        elif index == len(n)-1:
            out += ', and '+ value
        else:
            out += ', ' + value
    return out

spam = []
print(commaCode(spam))
