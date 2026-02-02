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

board = np.full((8,8), '_')

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

    pygame.display.update()