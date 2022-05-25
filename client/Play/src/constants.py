import os
import pygame
from bysnes import *
from base_constants import *

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

recept_of_petrol = Recept({LIST_OF_MATIRIAL[0] : 3, LIST_OF_MATIRIAL[1] : 0 }, {LIST_OF_MATIRIAL[0] : 0, LIST_OF_MATIRIAL[1] : 2 })
recept_of_oil = Recept({LIST_OF_MATIRIAL[0] : 0, LIST_OF_MATIRIAL[1] : 0 }, {LIST_OF_MATIRIAL[0] : 3, LIST_OF_MATIRIAL[1] : 0 })
neft = Bysnes('Нефтяная вышка', 1, recept_of_oil)
neft.get_offer(Contract(0, 1, LIST_OF_MATIRIAL[0], 10, 100)) # delete me
LIST_OF_BYSNES = [neft, Bysnes('заправка', 5, recept_of_petrol)]
