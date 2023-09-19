import pygame

class Button:
    def __init__(self, txt, pos):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (260, 40))

    def draw(self, screen, font):
        pygame.draw.rect(screen, 'light gray', self.button, 0, 5)
        pygame.draw.rect(screen, 'dark gray', self.button, 5, 5)
        text = font.render(self.text, True, 'black')
        screen.blit(text, (self.pos[0] + 15, self.pos[1] + 7))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True

        else:
            return False

def draw_game(screen, font):
    button = Button('Main Menu', (230, 450))
    button.draw(screen, font)
    return button.check_clicked()

def draw_menu(screen, font, width, button_name):
        command = 0
        button_width = 260
        button_height = 40
        spacing = 10
        total_button_height = (button_height + spacing) * 3 - spacing
        vertical_position = ((width - total_button_height) // 2) #gives y position
        buttons = [Button(name, [width // 2 - button_width // 2, vertical_position + i * (button_height + spacing)]) for i, name in enumerate(button_name)]
        for button in buttons:
             button.draw(screen, font)

        for i, button in enumerate(buttons):
             if button.check_clicked():
                  command = i + 1

        return command



