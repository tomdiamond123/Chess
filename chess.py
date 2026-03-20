import pygame
import numpy as np

pygame.init()

#Set Up Variables
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (78,120,55)
TAN = (238, 238, 210)
HIGHLIGHT = (144, 238, 144)
#Window dimension
DIMENSION = 800
SQUARESIZE = DIMENSION // 8


canvas = pygame.display.set_mode((DIMENSION,DIMENSION))
pygame.display.set_caption("Chess")

clock = pygame.time.Clock()

#Load Pieces
BLACKROOK = pygame.image.load('images/BlackRook.png').convert_alpha()
BLACKKNIGHT = pygame.image.load('images/BlackKnight.png').convert_alpha()
BLACKBISHOP = pygame.image.load('images/BlackBishop.png').convert_alpha()
BLACKQUEEN = pygame.image.load('images/BlackQueen.png').convert_alpha()
BLACKKING = pygame.image.load('images/BlackKing.png').convert_alpha()
BLACKPAWN = pygame.image.load('images/BlackPawn.png').convert_alpha()
WHITEROOK = pygame.image.load('images/WhiteRook.png').convert_alpha()
WHITEKNIGHT = pygame.image.load('images/WhiteKnight.png').convert_alpha()
WHITEBISHOP = pygame.image.load('images/WhiteBishop.png').convert_alpha()
WHITEQUEEN = pygame.image.load('images/WhiteQueen.png').convert_alpha()
WHITEKING = pygame.image.load('images/WhiteKing.png').convert_alpha()
WHITEPAWN = pygame.image.load('images/WhitePawn.png').convert_alpha()

#load circle
CIRCLE = pygame.image.load('images/circle.png').convert_alpha()
CIRCLEOUTLINE = pygame.image.load('images/circleoutline.png').convert_alpha()

# K is King and N is Knight
board = np.array([
    ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
    ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
    ["__", "__", "__", "__", "__", "__", "__", "__"],
    ["__", "__", "__", "__", "__", "__", "__", "__"],
    ["__", "__", "__", "__", "__", "__", "__", "__"],
    ["__", "__", "__", "__", "__", "__", "__", "__"],
    ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
    ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]
    ])
#board = np.flip(board)
# board = np.array([
#     ["BR", "__", "__", "__", "__", "BK", "__", "__"],
#     ["__", "__", "__", "__", "__", "__", "__", "__"],
#     ["__", "__", "__", "__", "__", "__", "__", "__"],
#     ["WP", "__", "BQ", "__", "BN", "__", "__", "__"],
#     ["__", "__", "__", "__", "__", "__", "__", "__"],
#     ["__", "__", "BB", "__", "__", "__", "__", "__"],
#     ["__", "__", "__", "__", "__", "__", "__", "__"],
#     ["__", "__", "__", "__", "__", "__", "__", "__"],
# ])

def displayBoard(colour1, colour2, highlight):
    for row in range(8):
        for col in range(8):
            if highlight is not None and (col, row) == highlight:
                colour = HIGHLIGHT
            elif (row+col)%2:
                colour = colour1
            else:
                colour = colour2
            pygame.draw.rect(canvas, colour, pygame.Rect(SQUARESIZE*col,SQUARESIZE*row,SQUARESIZE,SQUARESIZE))

def highlightSquare(side):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    col = mouse_x // SQUARESIZE
    row = mouse_y // SQUARESIZE
    if 0 <= row < 8 and 0 <= col < 8:
        if board[row][col][0] == side:
            return (col, row)
    return None

def getCurrentMouseSquare():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    col = mouse_x // SQUARESIZE
    row = mouse_y // SQUARESIZE
    if 0 <= row < 8 and 0 <= col < 8:
        return (col, row)
    return None

def displayPieces(board):
    for y, row in enumerate(board):
        for x, square in enumerate(row):
            if square == "BR":
                canvas.blit(BLACKROOK, (x*SQUARESIZE,y*SQUARESIZE))
            elif square == "BN":
                canvas.blit(BLACKKNIGHT, (x * SQUARESIZE, y * SQUARESIZE))
            elif square == "BB":
                canvas.blit(BLACKBISHOP, (x * SQUARESIZE, y * SQUARESIZE))
            elif square == "BQ":
                canvas.blit(BLACKQUEEN, (x * SQUARESIZE, y * SQUARESIZE))
            elif square == "BK":
                canvas.blit(BLACKKING, (x * SQUARESIZE, y * SQUARESIZE))
            elif square == "BP":
                canvas.blit(BLACKPAWN, (x * SQUARESIZE, y * SQUARESIZE))
            elif square == "WR":
                canvas.blit(WHITEROOK, (x * SQUARESIZE, y * SQUARESIZE))
            elif square == "WN":
                canvas.blit(WHITEKNIGHT, (x * SQUARESIZE, y * SQUARESIZE))
            elif square == "WB":
                canvas.blit(WHITEBISHOP, (x * SQUARESIZE, y * SQUARESIZE))
            elif square == "WQ":
                canvas.blit(WHITEQUEEN, (x * SQUARESIZE, y * SQUARESIZE))
            elif square == "WK":
                canvas.blit(WHITEKING, (x * SQUARESIZE, y * SQUARESIZE))
            elif square == "WP":
                canvas.blit(WHITEPAWN, (x * SQUARESIZE, y * SQUARESIZE))

def rookMoves(board, col, row):
    moves = []
    side = board[row][col][0]

    # Rook moves
    # up
    for r in range(row-1, -1, -1):
        sq = board[r][col]
        if sq == "__":
            moves.append((col, r))
        elif sq[0] != side:
            moves.append((col, r))
            break
        else:
            break
    # down
    for r in range(row+1, 8):
        sq = board[r][col]
        if sq == "__":
            moves.append((col, r))
        elif sq[0] != side:
            moves.append((col, r))
            break
        else:
            break
    # left
    for c in range(col-1, -1, -1):
        sq = board[row][c]
        if sq == "__":
            moves.append((c, row))
        elif sq[0] != side:
            moves.append((c, row))
            break
        else:
            break
    # right
    for c in range(col+1, 8):
        sq = board[row][c]
        if sq == "__":
            moves.append((c, row))
        elif sq[0] != side:
            moves.append((c, row))
            break
        else:
            break

    return moves

def bishopMoves(board, col, row):
    moves = []
    side = board[row][col][0]

    directions = [(-1, -1), (1, -1), (-1, 1), (1, 1)]

    for dc, dr in directions:
        r, c = row, col
        while True:
            r += dr
            c += dc
            if 0 <= r < 8 and 0 <= c < 8:
                sq = board[r][c]
                if sq == "__":
                    moves.append((c, r))
                elif sq[0] != side:
                    moves.append((c, r))
                    break
                else:
                    break
            else:
                break

    return moves

def knightMoves(board, col, row):
    moves = []
    side = board[row][col][0]

    directions = [(1,2), (2,1), (1,-2), (-1, 2), (-2, 1), (2, -1), (-2, -1), (-1, -2)]
    for dc, dr in directions:
        r, c = row, col
        r += dr
        c += dc
        if 0 <= r < 8 and 0 <= c < 8:
            sq = board[r][c]
            if sq == "__":
                moves.append((c, r))
            elif sq[0] != side:
                moves.append((c, r))
                continue
            else:
                continue
        else:
            continue
    
    return moves

def queenMoves(board, col, row):
    moves = []
    side = board[row][col][0]

    directions = [(-1, -1), (1, -1), (-1, 1), (1, 1), (1,0), (0,1), (-1,0), (0,-1)]

    for dc, dr in directions:
        r, c = row, col
        while True:
            r += dr
            c += dc
            if 0 <= r < 8 and 0 <= c < 8:
                sq = board[r][c]
                if sq == "__":
                    moves.append((c, r))
                elif sq[0] != side:
                    moves.append((c, r))
                    break
                else:
                    break
            else:
                break

    return moves

def pawnMoves(board, col, row):
    moves = []
    side = board[row][col][0]

    if board[row-1][col] == "__":
        moves.append((col, row-1))
    if col < 7:
        if board[row-1][col+1][0] != side and board[row-1][col+1] != "__":
            moves.append((col+1, row-1))
    if col > 0:
        if board[row-1][col-1][0] != side and board[row-1][col-1] != "__":
            moves.append((col-1, row-1))
    if row == 6:
        if board[row-2][col] == "__":
            moves.append((col, row-2))

    return moves

def pseudoLegalMoves(board, col, row):
    if board[row][col] == "__":
        return []

    piece = board[row][col][1]

    if piece == "R":
        return rookMoves(board, col, row)
    elif piece == "B":
        return bishopMoves(board, col, row)
    elif piece == "N":
        return knightMoves(board, col, row)
    elif piece == "Q":
        return queenMoves(board, col, row)
    elif piece == "P":
        return pawnMoves(board, col, row)
    elif piece == "K":
        moves = []
        side = board[row][col][0]
        directions = [(-1, -1), (1, -1), (-1, 1), (1, 1), (1,0), (0,1), (-1,0), (0,-1)]
        for dc, dr in directions:
            nc, nr = col + dc, row + dr
            if 0 <= nr < 8 and 0 <= nc < 8:
                sq = board[nr][nc]
                if sq == "__" or sq[0] != side:
                    moves.append((nc, nr))
        return moves

    return []


def findKing(board, side):
    for r in range(8):
        for c in range(8):
            if board[r][c] == side + "K":
                return (c, r)
    return None

def simulateMove(board, oldcol, oldrow, newcol, newrow):
    b2 = np.copy(board)
    b2[newrow][newcol] = b2[oldrow][oldcol]
    b2[oldrow][oldcol] = "__"
    return b2

def pawnAttacks(board, col, row):
    attacks = []
    side = board[row][col][0]
    dr = -1 if side == "W" else 1
    nr = row + dr
    if 0 <= nr < 8:
        if col - 1 >= 0:
            attacks.append((col - 1, nr))
        if col + 1 < 8:
            attacks.append((col + 1, nr))
    return attacks

def kingCheck(board, col, row, side):
    opponent = "B" if side == "W" else "W"

    for r_idx, row_data in enumerate(board):
        for c_idx, piece in enumerate(row_data):
            if piece == "__" or piece[0] != opponent:
                continue

            ptype = piece[1]

            if ptype == "R":
                attacks = rookMoves(board, c_idx, r_idx)
            elif ptype == "B":
                attacks = bishopMoves(board, c_idx, r_idx)
            elif ptype == "N":
                attacks = knightMoves(board, c_idx, r_idx)
            elif ptype == "Q":
                attacks = queenMoves(board, c_idx, r_idx)
            elif ptype == "P":
                attacks = pawnAttacks(board, c_idx, r_idx)
            elif ptype == "K":
                attacks = []
                directions = [(-1, -1), (1, -1), (-1, 1), (1, 1), (1,0), (0,1), (-1,0), (0,-1)]
                for dc, dr in directions:
                    nc, nr = c_idx + dc, r_idx + dr
                    if 0 <= nr < 8 and 0 <= nc < 8:
                        attacks.append((nc, nr))
            else:
                attacks = []

            if (col, row) in attacks:
                return True

    return False


def kingMoves(board, col, row):
    moves = []
    side = board[row][col][0]

    directions = [(-1, -1), (1, -1), (-1, 1), (1, 1), (1,0), (0,1), (-1,0), (0,-1)]

    for dc, dr in directions:
        try:
            if board[row+dr][col+dc] == "__" or board[row+dr][col+dc][0] != side:
                if not kingCheck(board, col+dc, row+dr, side):
                    moves.append((col+dc, row+dr))
        except IndexError:
            #Checking square that doesn't exist
            pass

    return moves

def calculateLegalMoves(board, col, row):
    if board[row][col] == "__":
        return [], False

    side = board[row][col][0]
    legal = []

    candidates = pseudoLegalMoves(board, col, row)

    for (nc, nr) in candidates:
        b2 = simulateMove(board, col, row, nc, nr)

        king_pos = findKing(b2, side)
        if king_pos is None:
            continue

        if not kingCheck(b2, king_pos[0], king_pos[1], side):
            legal.append((nc, nr))

    # gameOver detection is handled separately
    return legal, False


def allLegalMoves(board, side):
    """
    Generate all legal moves for the given side.
    Returns a list of tuples: (old_col, old_row, new_col, new_row)
    """
    moves = []
    for row in range(8):
        for col in range(8):
            if board[row][col] != "__" and board[row][col][0] == side:
                legal_moves, _ = calculateLegalMoves(board, col, row)
                for move in legal_moves:
                    moves.append((col, row, move[0], move[1]))
    return moves

def isCheckmate(board, side):
    """
    Returns True if the side is in checkmate.
    """
    # Find king position
    king_pos = None
    for r in range(8):
        for c in range(8):
            if board[r][c] == side + "K":
                king_pos = (c, r)
                break
        if king_pos:
            break
    
    if king_pos is None:
        # King missing, treat as game over (checkmate)
        return True
    
    # Check if king is in check
    if not kingCheck(board, king_pos[0], king_pos[1], side):
        return False  # Not in check, so not checkmate
    
    # Check if any legal move exists
    moves = allLegalMoves(board, side)
    if len(moves) == 0:
        return True
    return False

def isStalemate(board, side):
    """
    Returns True if the side is in stalemate.
    """
    # Find king position
    king_pos = None
    for r in range(8):
        for c in range(8):
            if board[r][c] == side + "K":
                king_pos = (c, r)
                break
        if king_pos:
            break
    
    if king_pos is None:
        # King missing, not stalemate
        return False
    
    # King not in check
    if kingCheck(board, king_pos[0], king_pos[1], side):
        return False
    
    # No legal moves available
    moves = allLegalMoves(board, side)
    if len(moves) == 0:
        return True
    return False

def anyLegalMoveExists(board, side):
    for r in range(8):
        for c in range(8):
            if board[r][c] != "__" and board[r][c][0] == side:
                moves, _ = calculateLegalMoves(board, c, r)
                if moves:
                    return True
    return False

def getGameState(board, side_to_move):
    king_pos = findKing(board, side_to_move)
    if king_pos is None:
        return "checkmate"

    in_check = kingCheck(board, king_pos[0], king_pos[1], side_to_move)
    has_moves = anyLegalMoveExists(board, side_to_move)

    if in_check and not has_moves:
        return "checkmate"
    if not in_check and not has_moves:
        return "stalemate"
    if in_check:
        return "check"
    return "ok"


def drawLegalMoves(moves):
    for move in moves:
        x, y = move
        if board[y][x] == "__":
            canvas.blit(CIRCLE, (x*SQUARESIZE+30, y*SQUARESIZE+30))
        else:
            canvas.blit(CIRCLEOUTLINE, (x*SQUARESIZE, y*SQUARESIZE))

def movePiece(board,newcol, newrow, oldcol, oldrow):
    board[newrow][newcol] = board[oldrow][oldcol]
    board[oldrow][oldcol] = "__"
    return board

#main loop
exit = False
mouseDown = False
highlightedSquare = None
highlighted = False
side = "W"

while not exit:
    canvas.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouseDown = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and mouseDown == True:
            mouseDown = False
            if getCurrentMouseSquare() in legalMoves:
                newcol, newrow = getCurrentMouseSquare()
                oldcol, oldrow = highlightedSquare
                board = movePiece(board, newcol, newrow, oldcol, oldrow)
                if side == "W":
                    side = "B"
                else:
                    side = "W"
                board = np.flipud(board)
                board = np.fliplr(board)
                highlightedSquare = None
                highlighted = False
                state = getGameState(board, side)
                
                if state == "checkmate":
                    print("Checkmate! Game over.")
                    #exit = True  # Or handle game over UI here
                elif state == "stalemate":
                    print("Stalemate! Game drawn.")
                    #exit = True
                elif state == "check":
                    print("Check!")
            elif highlightedSquare != highlightSquare(side) or highlightedSquare == None:
                highlightedSquare = highlightSquare(side)
                highlighted = True
            else:
                highlightedSquare = None
                highlighted = False
        
    displayBoard(GREEN,TAN, highlightedSquare)
    legalMoves, _ = (calculateLegalMoves(board, highlightedSquare[0], highlightedSquare[1]) if highlightedSquare and highlighted else ([], False))

    # Check for checkmate or stalemate after each move
    if isCheckmate(board, side):
        print(f"Checkmate! {'White' if side == 'B' else 'Black'} wins.")
        #exit = True  # or handle game over screen
    elif isStalemate(board, side):
        print("Stalemate! The game is a draw.")
        #exit = True  # or handle game over screen
    drawLegalMoves(legalMoves)
    displayPieces(board)

    pygame.display.update()
    clock.tick(60)