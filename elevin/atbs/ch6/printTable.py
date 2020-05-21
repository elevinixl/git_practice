def printTable(tableData):

    #Make list of max values
    colWidths = [0] * len(tableData)
    for i, v in enumerate(tableData):
        for item in v:
            colWidths[i] = max(colWidths[i],len(item)+1)

    printString = ''
    for x in range(len(tableData[0])):
        for i, v in enumerate(colWidths):
            printString += tableData[i][x].rjust(v)
        printString += '\n'

    print(printString)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)