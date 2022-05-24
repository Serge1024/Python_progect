import os
import pygame
from bysnes import *

game_folder = os.path.dirname(__file__)
resources_folder = game_folder + '/../resources'
img_folder = os.path.join(resources_folder, 'sprites')
fonts_folder = os.path.join(resources_folder, 'fonts')
logo_img = pygame.image.load(os.path.join(img_folder, 'MIPT.png'))
background_img = pygame.image.load(os.path.join(img_folder, 'background.png'))


# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (100, 100, 200)
RED = (200, 100, 100)
GREEN = (100, 200, 100)
SCREEN_COLOR = WHITE
BUTTON_COLOR = BLUE
FONT_COLOR = BLACK

LIST_OF_BYSNES = [Bysnes('Нефтяная вышка', 10, 10), Bysnes('заправка', 50, 5)]
