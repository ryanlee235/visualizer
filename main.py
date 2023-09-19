import pygame

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))






def main():
    run = True
    while run:
        for event in pygame.event():
            if event.type == pygame.QUIT:
                pygame.quit()


