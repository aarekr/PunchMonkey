""" User Interface module """

import sys
import pygame
import time
import random

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

BOARD_SIZE = (950, 750)
RADIUS = 50
DEFAULT_IMAGE_SIZE = (70, 70)

def game_top_text():
    """ Displaying Punch Monkey text """
    text_font = pygame.font.Font(pygame.font.get_default_font(), 60)
    game_starts = "Punch Monkey"
    label = text_font.render(game_starts, 0, RED)
    return label

def game_start_text():
    """ Displaying game start text """
    text_font = pygame.font.Font(pygame.font.get_default_font(), 40)
    game_starts = "Press s to start the game"
    label = text_font.render(game_starts, 0, BLUE)
    return label

class UI:
    """ User interface class """
    def __init__(self):
        self.game_active = True
        self.screen = pygame.display.set_mode(BOARD_SIZE)
        self.interval = 2
        self.points = 0

    def start_game(self):
        pygame.init()
        self.screen.blit(game_top_text(), (250, 15))
        self.screen.blit(game_start_text(), (210, 250))
        pygame.display.update()
        start_game = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        start_game = True
                        self.points = 0
            if start_game == True:
                break
        self.game_loop()
    
    def draw_ellipses(self):
        y = 200
        while y <= 700:
            x = 100
            while x <= 700:
                pygame.draw.ellipse(self.screen, BLACK, (x, y, 100, 20))
                x += 200
            y += 150
        pygame.display.update()

    def display_points(self):
        """ Displaying game points """
        text_font = pygame.font.Font(pygame.font.get_default_font(), 30)
        points_text = f"Points {self.points}"
        label = text_font.render(points_text, 0, BLUE)
        return label

    def draw_main_items(self):
        self.screen.fill(WHITE)
        self.screen.blit(game_top_text(), (250, 15))
        self.screen.blit(self.display_points(), (770, 20))
        self.draw_ellipses()

    def game_loop(self):
        pygame.init()
        self.screen.blit(game_top_text(), (250, 15))
        monkey_image = pygame.image.load("assets/monkey_eyes_covered.jpg")
        monkey_image = pygame.transform.scale(monkey_image, DEFAULT_IMAGE_SIZE)
        pygame.display.update()

        print("Game started")
        while self.game_active:
            self.draw_main_items()
            time.sleep(random.choice([1,2,3,4,5]))
            self.draw_main_items()
            self.interval -= 0.01
            x = random.choice([100, 300, 500, 700]) + 18
            y = random.choice([200, 350, 500, 650]) - 60
            self.screen.blit(monkey_image, (x,y))
            pygame.display.update()
            time.sleep(self.interval)
            loop_start = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_position = event.pos
                    print("clicked_position:", clicked_position)
                    print("monkey_position :", x, y)
                    print("x difference    :", clicked_position[0] - x)
                    print("y difference    :", clicked_position[1] - y)
                    if x <= clicked_position[0] <= x+70:
                        if y <= clicked_position[1] <= y+70:
                            print("hit")
                            loop_end = time.time()
                            self.points += 1
                    print("----------------------------------------")
