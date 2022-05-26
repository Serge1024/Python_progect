import os
import pygame
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

def recept_maker(dict_this_ingredient):
    answer = dict()
    for i in LIST_OF_MATIRIAL:
        answer[i] = 0
    for i in dict_this_ingredient.keys():
        answer[i] = dict_this_ingredient[i]
    return answer

recept_of_petrol = Recept(recept_maker({LIST_OF_MATIRIAL[0] : 3}), recept_maker({LIST_OF_MATIRIAL[1] : 2 }))
recept_of_oil = Recept(recept_maker(dict()), recept_maker({LIST_OF_MATIRIAL[0] : 3}))
recept_of_grass = Recept(recept_maker(dict()), recept_maker({LIST_OF_MATIRIAL[2] : 5}))
recept_of_meat = Recept(recept_maker({LIST_OF_MATIRIAL[1] : 10, LIST_OF_MATIRIAL[2] : 5}), recept_maker({LIST_OF_MATIRIAL[3] : 4}))

ferma = Bysnes('Ферма', 6, recept_of_meat, True, LIST_OF_MATIRIAL[3], 1)
pole = Bysnes('Поле', 2, recept_of_grass, False, LIST_OF_MATIRIAL[2], 2)
neft = Bysnes('Нефтяная вышка', 1, recept_of_oil, False, LIST_OF_MATIRIAL[0], 3)
zapravka = Bysnes('заправка', 5, recept_of_petrol, True, LIST_OF_MATIRIAL[1], 2)

LIST_OF_BYSNES = [neft, zapravka, pole, ferma]
