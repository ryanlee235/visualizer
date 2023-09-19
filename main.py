import pygame
from menu import draw_game, draw_menu
from search import draw_grid
pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("algorithm vizualizer")
fps = 60 
timer =pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 24)
start_menu = ["Search Algorithms", "Sorting Algortihms", "Exit"]

search = ["Linear Search", "Binary Search", "Deapth-first-search", "Breadth-first-search", "A*"]
sorting = ["Bubble sort", "Selection sort", "Insertion sort", "Quick sort", "Merge sort", "Heap sort"]


def main():
    run = True
    main_menu = True
    s = False
    sorting_menu = False
    main_command = 0
    search_command = 0
    sorting_command = 0
    rows = 25
    while run:
        screen.fill("gray")
        timer.tick(fps)

        if main_menu:
            main_command = draw_menu(screen, font, WIDTH, start_menu)
            
            if main_command == 1:
                main_menu = False
                s = True
            elif main_command == 2:
                sorting_menu = True
                main_menu = False

            elif main_command == 3:
                pygame.quit()

        if s:
            search_command = draw_menu(screen, font, WIDTH, search)

        if sorting_menu:
            sorting_command = draw_menu(screen, font, WIDTH, sorting)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()