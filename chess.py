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
# board = np.array([
#     ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
#     ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
#     ["__", "__", "__", "__", "__", "__", "__", "__"],
#     ["__", "__", "__", "__", "__", "__", "__", "__"],
#     ["__", "__", "__", "__", "__", "__", "__", "__"],
#     ["__", "__", "__", "__", "__", "__", "__", "__"],
#     ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
#     ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]
#     ])
#board = np.flip(board)
board = np.array([
    ["BR", "__", "__", "__", "__", "BK", "__", "__"],
    ["__", "__", "__", "__", "__", "__", "__", "__"],
    ["__", "__", "__", "__", "__", "__", "__", "__"],
    ["WP", "__", "BQ", "__", "BN", "__", "__", "__"],
    ["__", "__", "__", "__", "__", "__", "__", "__"],
    ["__", "__", "BB", "__", "__", "__", "__", "__"],
    ["__", "__", "__", "__", "__", "__", "__", "__"],
    ["__", "__", "__", "__", "__", "__", "__", "__"],
])

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

def highlightSquare():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    col = mouse_x // SQUARESIZE
    row = mouse_y // SQUARESIZE
    if 0 <= row < 8 and 0 <= col < 8:
        if board[row][col] != "__":
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

def kingMoves(board, col, row):
    moves = []
    side = board[row][col][0]

    directions = [(-1, -1), (1, -1), (-1, 1), (1, 1), (1,0), (0,1), (-1,0), (0,-1)]

    for dc, dr in directions:
        if board[row+dr][col+dc] == "__" or board[row+dr][col+dc] != side:
            moves.append((col+dc, row+dr))

    return moves

def calculateLegalMoves(board, col, row):
    moves = []
    if board[row][col] == "__":
        return moves
    side = board[row][col][0]
    piece = board[row][col][1]

    if piece == "R":
        moves.extend(rookMoves(board, col, row))
    elif piece == "B":
        moves.extend(bishopMoves(board, col, row))
    elif piece == "N":
        moves.extend(knightMoves(board, col, row))
    elif piece == "Q":
        moves.extend(queenMoves(board, col, row))
    elif piece == "P":
        moves.extend(pawnMoves(board, col, row))
    elif piece == "K":
        moves.extend(kingMoves(board, col, row))

    return moves

def drawLegalMoves(moves):
    for move in moves:
        x, y = move
        if board[y][x] == "__":
            canvas.blit(CIRCLE, (x*SQUARESIZE+30, y*SQUARESIZE+30))
        else:
            canvas.blit(CIRCLEOUTLINE, (x*SQUARESIZE, y*SQUARESIZE))



#main loop
exit = False
mouseDown = False
highlightedSquare = None
highlighted = False

while not exit:
    canvas.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouseDown = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and mouseDown == True:
            mouseDown = False
            if highlightedSquare != highlightSquare() or highlightedSquare == None:
                highlightedSquare = highlightSquare()
                highlighted = True
            else:
                highlightedSquare = None
                highlighted = False
        

    displayBoard(GREEN,TAN, highlightedSquare)
    legalMoves = calculateLegalMoves(board, highlightedSquare[0], highlightedSquare[1]) if highlightedSquare and highlighted else []
    drawLegalMoves(legalMoves)
    displayPieces(board)

    pygame.display.update()
    clock.tick(60)