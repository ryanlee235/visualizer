import pygame


class Node:
    def __init__(self):
        pass
    
    
def draw_grid(screen, rows, width):
    gap = width // rows

    for x in range(rows):
        pygame.draw.line(screen, "black", (0, x * gap), (width, x*gap))
        for y in range(rows):
            pygame.draw.line(screen, "black", (y*gap, 0), (y* gap, width))