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

#Load Pieces
BLACKROOK = pygame.image.load('pieces/BlackRook.png').convert_alpha()
BLACKKNIGHT = pygame.image.load('pieces/BlackKnight.png').convert_alpha()
BLACKBISHOP = pygame.image.load('pieces/BlackBishop.png').convert_alpha()
BLACKQUEEN = pygame.image.load('pieces/BlackQueen.png').convert_alpha()
BLACKKING = pygame.image.load('pieces/BlackKing.png').convert_alpha()
BLACKPAWN = pygame.image.load('pieces/BlackPawn.png').convert_alpha()
WHITEROOK = pygame.image.load('pieces/WhiteRook.png').convert_alpha()
WHITEKNIGHT = pygame.image.load('pieces/WhiteKnight.png').convert_alpha()
WHITEBISHOP = pygame.image.load('pieces/WhiteBishop.png').convert_alpha()
WHITEQUEEN = pygame.image.load('pieces/WhiteQueen.png').convert_alpha()
WHITEKING = pygame.image.load('pieces/WhiteKing.png').convert_alpha()
WHITEPAWN = pygame.image.load('pieces/WhitePawn.png').convert_alpha()

# K is King and N is Knight
board = np.array([
    ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
    ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
    ["_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_"],
    ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
    ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]
    ])
#board = np.flip(board)

def displayBoard(colour1, colour2, highlight):
    for row in range(8):
        for col in range(8):
            if highlight is not None and (row, col) == highlight:
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
        return (row, col)
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



#main loop
exit = False
mouseDown = False
highlightedSquare = None

while not exit:
    canvas.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouseDown = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and mouseDown == True:
            mouseDown = False
            highlightedSquare = highlightSquare()
        

    displayBoard(GREEN,TAN, highlightedSquare)
    displayPieces(board)

    pygame.display.update()