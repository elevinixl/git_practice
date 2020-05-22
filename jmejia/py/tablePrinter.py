table = [['Alice', 'Bob', 'Carol', 'David'],
         ['apples', 'oranges', 'cherries', 'bananas'],
         ['dogs', 'cats', 'moose', 'goose']]


def printTable(tableData):
    maxWidth = 0
    for col in tableData:
        for item in col:
            maxWidth = max(maxWidth,len(item))

    spacing = maxWidth + 3
    for y in range(len(tableData[0])):
        for x in range(len(tableData)):
            print(tableData[x][y].rjust(spacing,' '), end='')
        print()


printTable(table)
