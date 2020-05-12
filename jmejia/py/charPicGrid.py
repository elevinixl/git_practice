grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# printCPG(x) assumes x is a list of rows
def printCPG(aGrid):
    for y, row in enumerate(aGrid):
        for x, char in enumerate(row):
            print(char, end='')
        print()
    return

# printCPG2(x) assumes x is a list of columns
def printCPG2(aGrid):
    for y in range(len(aGrid[0])):
        for x in range(len(aGrid)):
            print(aGrid[x][y], end='')
        print()
    return

printCPG(grid)
print('\n')
printCPG2(grid)