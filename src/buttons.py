from graphics import *
from dollar import *


class Button(pygame.sprite.Sprite):
    def __init__(self, position, text, size, height):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.image = pygame.Surface(size)
        self.image.fill(BUTTON_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.font = pygame.font.Font(fonts_folder + '/Font.ttf', int(height / 20))

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, self.rect, 0)
        pygame.draw.rect(surface, WHITE, self.rect, 2)
        text_surface = self.font.render(self.text, False, FONT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.rect.left + 10, self.rect.top + self.rect.height * 0.25)
        surface.blit(text_surface, text_rect)


class CurrencyButton(Button):
    def __init__(self, pos, text, size, height):
        super().__init__(pos, text, size, height)
        self.rect = Button(pos, text, size, height).rect
        self.count = 0
        self.text = text
        self.color = GREEN
        self.border_color = BLACK
        self.currency = Currency()
        self.last_time = pygame.time.get_ticks()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 0)
        pygame.draw.rect(surface, self.border_color, self.rect, 2)
        text_surface = FONT.render("Обменять по курсу: $1 = " + str(self.currency.get_exchange_rate()) + "RUB", False, FONT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.rect.left + 10, self.rect.top + self.rect.height * 0.25)
        surface.blit(text_surface, text_rect)

    def click(self, rub_score, dollar_score):
        if dollar_score > 0:
            rub_score += dollar_score * self.currency.get_exchange_rate()
            dollar_score = 0
        return rub_score, dollar_score


# CPS means Clicks per second
class UpgradeCPS(Button):
    def __init__(self, pos, text, size, height):
        super().__init__(pos, text, size, height)
        self.rect = Button(pos, text, size, height).rect
        self.count = 0
        self.text = text
        self.color = RED
        self.border_color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 0)
        pygame.draw.rect(surface, self.border_color, self.rect, 2)
        text_surface = FONT.render(" " + str(self.text), False, FONT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.rect.left + 10, self.rect.top + self.rect.height * 0.25)
        surface.blit(text_surface, text_rect)

    def click(self, auto_clicks, rub_score):
        print("Lol")
        return 0, 0


# CPC means clicks per click
class UpgradeCPC(Button):
    def __init__(self, pos, text, price, size, height):
        super().__init__(pos, text, size, height)
        self.rect = Button(pos, text, size, height).rect
        self.count = 0
        self.text = text
        self.price = price
        self.color = RED
        self.border_color = BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 0)
        pygame.draw.rect(surface, self.border_color, self.rect, 2)
        text_surface = FONT.render(" " + str(self.text), False, FONT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.rect.left + 10, self.rect.top + self.rect.height * 0.25)
        surface.blit(text_surface, text_rect)

    def click(self, booster, dollar_score):
        if dollar_score >= self.price:
            self.count += 1
            dollar_score -= self.price
            booster += 1
            self.price *= 1.2
            self.price = int(self.price)
        return booster, dollar_score

    def check_if_available(self, dollar_score):
        if self.price <= dollar_score:
            self.color = BLUE
            return True
        else:
            self.color = RED
            return False


def initiate_buttons(width, height):
    upgrade_cpc = UpgradeCPC((width / 4,  height / 6),UPGRADES_LIST[0][0], 1, (width * 3 / 8, height / 12), height)
    upgrade_cps = UpgradeCPS((width / 4 + width / 2,  height / 6), UPGRADES_LIST[0][1], (width * 3 / 8, height / 12), height)

    main_menu = [Button((width / 2, 2 * height / 3), "Settings", (width / 4, height / 6), height),
                 Button((width / 2, height / 3), "Play!", (width / 4, height / 6), height)]

    settings = [Button((width / 3, 2 * height / 3), "FullScreen", (width / 4, height / 6), height),
                Button((2 * width / 3, height / 3), "800 x 600", (width / 4, height / 6), height),
                Button((2 * width / 3, 2 * height / 3), "1200 x 900", (width / 4, height / 6), height),
                Button((width / 3, height / 3), "Back", (width / 4, height / 6), height)]

    currency = [CurrencyButton((31 * width / 60, height / 16), "", (width * 3 / 8, height / 12), height)]
    return upgrade_cpc, upgrade_cps, main_menu, settings, currency
