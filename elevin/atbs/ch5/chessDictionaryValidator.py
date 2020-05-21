def isValidChessBoard(board):

    pieces = {}
    wpieces = 0
    bpieces = 0
    for piece in board.values():
        pieces.setdefault(piece,0)
        pieces[piece] += 1
        if piece[0] == 'w':
            wpieces += 1
        elif piece[0] == 'b':
            bpieces += 1

    # Checks for 1 king
    if pieces['bking'] != 1 or pieces['wking'] != 1:
        return False

    # Checks for <=16 pieces
    if wpieces > 16 or bpieces > 16:
        return False

    # Checks for <=8 pawns
    if pieces.get('bpawn',0) > 8 or pieces.get('bpawn',0)  > 8:
        return False

    #Checks for valid spaces
    for space in board:
        if int(space[0]) not in range(1,9):
            return False
        elif space[1] not in ['a','b','c','d','e','f','g','h']:
            return False

    return True

example = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(example))