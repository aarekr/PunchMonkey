""" User Interface module """

import sys
import pygame

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

BOARD_SIZE = (950, 750)
RADIUS = 50

def game_start_text():
    """ Displaying game start text """
    text_font = pygame.font.Font(pygame.font.get_default_font(), 60)
    game_starts = "Punch Monkey"
    label = text_font.render(game_starts, 0, YELLOW)
    return label

class UI:
    """ User interface class """
    def __init__(self):
        self.game_active = True
        self.screen = pygame.display.set_mode(BOARD_SIZE)

    def start_game(self):
        self.game_loop()
    
    def draw_ellipses(self):
        y = 200
        while y <= 700:
            x = 100
            while x <= 700:
                pygame.draw.ellipse(self.screen, WHITE, (x, y, 100, 20))
                x += 200
            y += 150
        pygame.display.update()

    def game_loop(self):
        pygame.init()
        self.screen.blit(game_start_text(), (250, 15))
        #self.draw_ellipses()
        pygame.display.update()

        print("Game started")
        while self.game_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self.draw_ellipses()
