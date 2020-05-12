import re

def isValidChessBoard(board):
    # Check that there is exactly 1 black and white king
    if list(board.values()).count('bking') != 1:
        return False
    if list(board.values()).count('wking') != 1:
        return False

    # Check that there are no more than 8 black or white pawns
    if list(board.values()).count('bpawn') > 8:
        return False
    if list(board.values()).count('wpawn') > 8:
        return False

    posRE = re.compile(r'^[1-8][a-h]$')
    pieceRE = re.compile(r'^[wb](pawn|knight|bishop|rook|queen|king)$')
    wCount = 0
    bCount = 0
    for pos,piece in board.items():
        # Check that all positions are valid (/[1-8][a-h]/)
        if not posRE.search(pos):
            return False
        # Check that all pieces are valid (/[wb](pawn|knight|bishop|rook|queen|king)/)
        if not pieceRE.search(piece):
            return False
        if piece[0] == 'w':
            wCount += 1
        else:
            bCount += 1
    # Check that neither white nor black have more than 16 total pieces (values start with 'w' or 'b')
    if (wCount > 16) or (bCount > 16):
        return False

    return True


test = {'aa':'11', 'bb':'22', 'cc':'33', 'dd':'11'}
test2 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

print(isValidChessBoard(test))
print(isValidChessBoard(test2))