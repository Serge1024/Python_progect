from buttons import *


class Game:
    def __init__(self):
        pygame.display.set_caption("MIPT clicker")
        self.clock = pygame.time.Clock()
        self.running = True
        self.logo = Logo((WIDTH / 10, 23 * HEIGHT / 24), WIDTH, HEIGHT)
        self.background = Background((WIDTH / 2, HEIGHT / 2), WIDTH, HEIGHT)
        self.font = pygame.font.Font(fonts_folder + '/Font.ttf', 20)
        self.font2 = pygame.font.Font(fonts_folder + '/Font.ttf', 40)
        self.upgradesCPC, self.upgradesCPS, self.menu_buttons, self.settings_buttons, self.currency_button, self.bysnes_button, self.back_bysnes, self.my_bysnes_button = initiate_buttons(WIDTH, HEIGHT)
        self.menu_running = True
        self.settings_running = True
        self.rub_score = 0
        self.dollar_score = 0
        self.booster = 1
        self.auto_clicks = 0
        self.prev_tick = 0
        self.my_bysnes = list()

    def render_main(self):
        SCREEN.fill(SCREEN_COLOR)
        SCREEN.blit(self.background.image, self.background.rect)
        SCREEN.blit(self.logo.image, self.logo.rect)
        self.upgradesCPC.draw(SCREEN)
        self.upgradesCPC.check_if_available(self.dollar_score)
        self.upgradesCPS.draw(SCREEN)
        self.currency_button[0].draw(SCREEN)
        text_score_dollar = self.font.render("$" + str(self.dollar_score), True, FONT_COLOR)
        text_score_rub = self.font.render("Your wallet:  " + str(self.rub_score) + "RUB", True, FONT_COLOR)
        text_upgr_1 = self.font.render("$ per CLICK: " + str(self.booster), True, FONT_COLOR)
        text_upgr_2 = self.font.render("$ per SEC: " + str(self.auto_clicks), True, FONT_COLOR)
        SCREEN.blit(text_score_dollar, (WIDTH / 20, HEIGHT / 20 + 200))
        SCREEN.blit(text_score_rub, (10 * WIDTH / 14, HEIGHT / 20 + 200))
        SCREEN.blit(text_upgr_1, (WIDTH / 20, HEIGHT / 20))
        SCREEN.blit(text_upgr_2, (10 * WIDTH / 14, HEIGHT / 20))
        pygame.display.flip()

    def render_menu(self):
        SCREEN.fill(BLACK)
        for i in self.menu_buttons:
            i.draw(SCREEN)
        pygame.display.flip()

    def render_settings(self):
        SCREEN.fill(BLACK)
        for i in self.settings_buttons:
            i.draw(SCREEN)
        pygame.display.flip()

    def check_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.menu_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in self.menu_buttons:
                    if button.rect.collidepoint(event.pos):
                        if button.text == "Play!":
                            self.menu_running = False
                        elif button.text == "Settings":
                            self.settings_running = True
                            while self.settings_running:
                                self.render_settings()
                                self.check_settings_event()

    def change_screen_size(self):
        global FONT
        FONT = pygame.font.Font(fonts_folder + '/Font.ttf', int(HEIGHT / 40))
        self.upgradesCPC, self.upgradesCPS, self.menu_buttons, self.settings_buttons, self.currency_button = initiate_buttons(WIDTH, HEIGHT)
        self.logo = Logo((WIDTH / 10, 23 * HEIGHT / 24), WIDTH, HEIGHT)
        self.background = Background((WIDTH / 2, HEIGHT / 2), WIDTH, HEIGHT)
        self.font = pygame.font.Font(fonts_folder + '/Font.ttf', int(WIDTH / 45))
        self.font2 = pygame.font.Font(fonts_folder + '/Font.ttf', int(WIDTH / 20))

    def check_settings_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.menu_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                global WIDTH
                global HEIGHT
                global SCREEN
                for button in self.settings_buttons:
                    if button.rect.collidepoint(event.pos):
                        if button.text == "FullScreen":
                            WIDTH = 1920
                            HEIGHT = 1080
                        elif button.text == "800 x 600":
                            WIDTH = 800
                            HEIGHT = 600
                        elif button.text == "1200 x 900":
                            WIDTH = 1200
                            HEIGHT = 900
                        elif button.text == "Back":
                            self.settings_running = False
                        self.change_screen_size()
                        SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

    def render_my_bysnes(self):
        for i in self.my_bysnes_button:
            i.draw(SCREEN)

        
    def check_events_my_bysnes(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.bysnes_running = False
                self.my_bysnes_flag = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # escape is pressed
                    self.running = False
                    self.bysnes_running = False
                    self.my_bysnes_flag = False

    def render_bysnes(self):
        SCREEN.fill(SCREEN_COLOR)
        SCREEN.blit(self.background.image, self.background.rect)
        SCREEN.blit(self.logo.image, self.logo.rect)
        for i in self.bysnes_button:
            i.draw(SCREEN)
            i.check_if_available(self.dollar_score)
        self.back_bysnes.draw(SCREEN)
        self.my_bysnes_button.draw(SCREEN)
        self.currency_button[0].draw(SCREEN)
        text_score_dollar = self.font.render("$" + str(self.dollar_score), True, FONT_COLOR)
        text_score_rub = self.font.render("Your wallet:  " + str(self.rub_score) + "RUB", True, FONT_COLOR)
        text_upgr_1 = self.font.render("$ per CLICK: " + str(self.booster), True, FONT_COLOR)
        text_upgr_2 = self.font.render("$ per SEC: " + str(self.auto_clicks), True, FONT_COLOR)
        SCREEN.blit(text_score_dollar, (WIDTH / 20, HEIGHT / 20 + 200))
        SCREEN.blit(text_score_rub, (10 * WIDTH / 14, HEIGHT / 20 + 200))
        SCREEN.blit(text_upgr_1, (WIDTH / 20, HEIGHT / 20))
        SCREEN.blit(text_upgr_2, (10 * WIDTH / 14, HEIGHT / 20))
        pygame.display.flip()

    def check_events_bysnes(self):        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.bysnes_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # escape is pressed
                    self.running = False
                    self.bysnes_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i in self.bysnes_button:
                    if (i.rect.collidepoint(event.pos) and i.clicable(self.dollar_score)):
                        bysnes, self.dollar_score = i.click(self.dollar_score)
                        self.my_bysnes.append(bysnes)
                if (self.back_bysnes.rect.collidepoint(event.pos)):
                    self.bysnes_running = False
                if (self.my_bysnes_button.rect.collidepoint(event.pos)):
                    self.my_bysnes_flag = True
                    self.my_bysnes_button = init_list_this_button(self.my_bysnes, WIDTH, HEIGHT)
                    while (self.my_bysnes_flag):
                        self.render_my_bysnes()
                        self.check_events_my_bysnes()


    def check_events(self):
        if pygame.time.get_ticks() - self.prev_tick >= 1000:
            self.dollar_score += self.auto_clicks
            self.prev_tick = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # space button is pressed
                    self.dollar_score += self.booster
                elif event.key == pygame.K_ESCAPE:  # escape is pressed
                    self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # right mouse click
                if self.upgradesCPS.rect.collidepoint(event.pos):
                    self.auto_clicks, self.rub_score = self.upgradesCPS.click(self.auto_clicks, self.rub_score)
                    self.bysnes_running = True
                    while (self.bysnes_running):
                        self.render_bysnes()
                        self.check_events_bysnes()

                if self.upgradesCPC.rect.collidepoint(event.pos):
                    self.booster, self.dollar_score = self.upgradesCPC.click(self.booster, self.dollar_score)
                if self.currency_button[0].rect.collidepoint(event.pos):
                    self.rub_score, self.dollar_score = self.currency_button[0].click(self.rub_score, self.dollar_score)

    def game_end(self):
        while self.running:
            self.render_win()
            self.check_events()

    def game_loop(self):
        while self.menu_running:
            self.render_menu()
            self.check_menu_events()

        while self.running:
            self.clock.tick(FPS)
            self.check_events()
            self.render_main()
