import buttons as b
import copy as copy


class Game:
    def __init__(self):
        pygame.display.set_caption("MIPT clicker")
        self.clock = pygame.time.Clock()
        self.running = True
        self.logo = Logo((WIDTH / 10, 23 * HEIGHT / 24), WIDTH, HEIGHT)
        self.background = Background((WIDTH / 2, HEIGHT / 2), WIDTH, HEIGHT)
        self.font = pygame.font.Font(fonts_folder + '/Font.ttf', 20)
        self.font2 = pygame.font.Font(fonts_folder + '/Font.ttf', 40)
        self.upgradesCPC, self.upgradesCPS, self.menu_buttons, self.settings_buttons, self.currency_button, self.bysnes_button, self.back_bysnes, self.my_bysnes_button, self.YES_button, self.NO_button, self.text_pole_make_offer, self.make_offer_button, self.add_button, self.add_worker = b.initiate_buttons(WIDTH, HEIGHT)
        self.menu_running = True
        self.settings_running = True
        self.rub_score = 0
        self.dollar_score = 0
        self.booster = 1
        self.auto_clicks = 0
        self.prev_tick = 0
        self.my_bysnes = list()
        self.bysnes_id = 1

    def render_main(self):
        SCREEN.fill(SCREEN_COLOR)
        SCREEN.blit(self.background.image, self.background.rect)
        SCREEN.blit(self.logo.image, self.logo.rect)
        text = self.upgradesCPC.text
        self.upgradesCPC.text += " $ 1"
        self.upgradesCPC.draw(SCREEN)
        self.upgradesCPC.check_if_available(self.dollar_score)
        self.upgradesCPC.text = text
        self.upgradesCPS.draw(SCREEN)
        text_score_dollar = self.font.render("$" + str(self.dollar_score), True, FONT_COLOR)
        SCREEN.blit(text_score_dollar, (WIDTH / 20, HEIGHT / 20 + 200))
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

    def render_my_own_bysnes(self, bysnes):
        list_of_nes = list()
        for i in bysnes.recept.ingredient.items():
            if (i[1] != 0):
                list_of_nes.append(i)
        string_of_nes = str()
        for i in list_of_nes:
            string_of_nes += i[0] + ' ' + str(i[1])

        SCREEN.fill(SCREEN_COLOR)
        SCREEN.blit(self.background.image, self.background.rect)
        SCREEN.blit(self.logo.image, self.logo.rect)
        self.back_bysnes.draw(SCREEN)
        self.make_offer_button.draw(SCREEN)
        self.add_button.draw(SCREEN)
        self.add_worker.draw(SCREEN)
        LIST_THIS_PODPIS = ["id", 'what', 'How math', 'cost']
        for i in self.text_pole_make_offer:
            i.draw(SCREEN)
        podpis = self.font.render(LIST_THIS_PODPIS[0], True, FONT_COLOR)
        SCREEN.blit(podpis, (WIDTH / 20 + 350, HEIGHT / 20 + 100))

        podpis = self.font.render(LIST_THIS_PODPIS[1], True, FONT_COLOR)
        SCREEN.blit(podpis, (WIDTH / 20 + 450, HEIGHT / 20 + 100))

        podpis = self.font.render(LIST_THIS_PODPIS[2], True, FONT_COLOR)
        SCREEN.blit(podpis, (WIDTH / 20 + 525, HEIGHT / 20 + 100))

        podpis = self.font.render(LIST_THIS_PODPIS[3], True, FONT_COLOR)
        SCREEN.blit(podpis, (WIDTH / 20 + 650, HEIGHT / 20 + 100))
        draw_string = ''
        for i in bysnes.sclad.items():
            draw_string += i[0] + ' ' + str(i[1]) + ' '
        text_sclad = self.font.render(draw_string, True, FONT_COLOR)
        SCREEN.blit(text_sclad, (WIDTH / 20, HEIGHT / 20 + 200))
        text_sclad = self.font.render("??????????", True, FONT_COLOR)
        SCREEN.blit(text_sclad, (WIDTH / 20, HEIGHT / 20 + 150))
        text_recept = self.font.render(string_of_nes, True, FONT_COLOR)
        SCREEN.blit(text_recept, (WIDTH / 20, HEIGHT / 20 + 300))

        text_recept = self.font.render("$ : " + str(bysnes.cost_of_work), True, FONT_COLOR)
        SCREEN.blit(text_recept, (WIDTH / 20, HEIGHT / 20 + 350))

        text_recept = self.font.render("$_SCORE " + str(bysnes.rub_score), True, FONT_COLOR)
        SCREEN.blit(text_recept, (WIDTH / 20 + 100, HEIGHT / 20 + 350))

        text_recept = self.font.render("count worker " + str(bysnes.work_resurce), True, FONT_COLOR)
        SCREEN.blit(text_recept, (WIDTH / 20, HEIGHT / 20 + 400))


        text_recept = self.font.render("add dollar", True, FONT_COLOR)
        SCREEN.blit(text_recept, (WIDTH / 20 - 10, HEIGHT / 20))


        text_recept = self.font.render("?????????????????????? ??????????????????", True, FONT_COLOR)
        SCREEN.blit(text_recept, (WIDTH / 20, HEIGHT / 20 + 250))

        text_bysnes_id = self.font.render("bysnes_id" + str(bysnes.bysnes_id), True, FONT_COLOR)
        SCREEN.blit(text_bysnes_id, (WIDTH / 20 + 300, HEIGHT / 20 ))
        if (len(bysnes.offer)):
            self.YES_button.draw(SCREEN)
            self.NO_button.draw(SCREEN)
            offer = bysnes.offer[0]
            text_offer = self.font.render("from " + str(offer.bysnes_id_from) + " " + offer.name + " " + str(offer.count), True, FONT_COLOR)
            SCREEN.blit(text_offer, (WIDTH / 20 + 500, HEIGHT / 20 + 200 ))
            text_offer = self.font.render( " cost " + str(offer.cost) , True, FONT_COLOR)
            SCREEN.blit(text_offer, (WIDTH / 20 + 500, HEIGHT / 20 + 250 ))

        pygame.display.flip()

    def check_events_my_own_bysnes(self, bysnes):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.bysnes_running = False
                self.my_bysnes_flag = False
                self.my_own_bysnes = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # escape is pressed
                    self.running = False
                    self.bysnes_running = False
                    self.my_bysnes_flag = False
                    self.my_own_bysnes = False
                else:
                    if event.key == pygame.K_BACKSPACE:
                        self.user_text = self.user_text[:-1]
                    else:
                        self.user_text += event.unicode
                    self.text_pole_make_offer[self.now_write_in].text = self.user_text

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if (self.back_bysnes.rect.collidepoint(event.pos)):
                    self.my_own_bysnes = False
                    for i in self.text_pole_make_offer:
                        i.text = ''
                if (self.YES_button.rect.collidepoint(event.pos)):
                    dec_of_dollar, ans_to_buyer = bysnes.say_yes()
                    self.dollar_score += dec_of_dollar
                    if (dec_of_dollar != 0):
                        import server
                        server.server.send_ans(ans_to_buyer)
                if (self.NO_button.rect.collidepoint(event.pos)):
                    import server
                    server.server.send_ans(bysnes.say_no())
                for i in range(5):
                    if (self.text_pole_make_offer[i].rect.collidepoint(event.pos)):
                        self.now_write_in = i
                        self.user_text = ''
                if (self.make_offer_button.rect.collidepoint(event.pos)):
                    helper = self.text_pole_make_offer[0 : 4]
                    offer = Contract(bysnes.bysnes_id, int(helper[3].text), LIST_OF_MATIRIAL[int(helper[2].text)], int(helper[1].text), int(helper[0].text))
                    for i in helper:
                        i.text = ''
                    if (offer.cost <= self.dollar_score):
                        self.dollar_score -= offer.cost
                        import server
                        server.server.put_contract(offer)
                if (self.add_button.rect.collidepoint(event.pos)):
                    if (self.dollar_score >= int(self.text_pole_make_offer[4].text)):
                        self.dollar_score -= int(self.text_pole_make_offer[4].text)
                        bysnes.add_rub(int(self.text_pole_make_offer[4].text))
                    self.text_pole_make_offer[4].text = ''
                if (self.add_worker.rect.collidepoint(event.pos)):
                    if (self.dollar_score >= price_of_worker):
                        bysnes.add_worker()
                        self.dollar_score -= price_of_worker



    def render_my_bysnes(self):
        SCREEN.fill(SCREEN_COLOR)
        SCREEN.blit(self.background.image, self.background.rect)
        SCREEN.blit(self.logo.image, self.logo.rect)
        for i in self.my_bysnes_buttons:
            i.draw(SCREEN)
        self.back_bysnes.draw(SCREEN)
        pygame.display.flip()

    

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
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if (self.back_bysnes.rect.collidepoint(event.pos)):
                    self.my_bysnes_flag = False
                for i in self.my_bysnes_buttons:
                    if (i.rect.collidepoint(event.pos)):
                        self.my_own_bysnes = True
                        self.now_write_in = 0
                        while(self.my_own_bysnes):
                            self.render_my_own_bysnes(i.bysnes)
                            self.check_events_my_own_bysnes(i.bysnes)



    def render_bysnes(self):
        SCREEN.fill(SCREEN_COLOR)
        SCREEN.blit(self.background.image, self.background.rect)
        SCREEN.blit(self.logo.image, self.logo.rect)
        for i in self.bysnes_button:
            text = i.text
            i.text += " $ " + str(i.bysnes.price)
            i.draw(SCREEN)
            i.check_if_available(self.dollar_score)
            i.text = text
        self.back_bysnes.draw(SCREEN)
        self.my_bysnes_button.draw(SCREEN)
        text_score_dollar = self.font.render("$" + str(self.dollar_score), True, FONT_COLOR)
        SCREEN.blit(text_score_dollar, (WIDTH / 20, HEIGHT / 20 + 200))
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
                        self.my_bysnes.append(copy.deepcopy(bysnes))
                        self.my_bysnes[-1].bysnes_id = self.bysnes_id
                        import server
                        server.server.data_base[self.bysnes_id] = (server.user_name, len(self.my_bysnes) - 1)
                        self.bysnes_id += 1

                if (self.back_bysnes.rect.collidepoint(event.pos)):
                    self.bysnes_running = False
                if (self.my_bysnes_button.rect.collidepoint(event.pos)):
                    self.my_bysnes_flag = True
                    self.my_bysnes_buttons = init_list_this_button(self.my_bysnes, WIDTH, HEIGHT)
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
                    for i in self.my_bysnes:
                        i.work()
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
def run():
    global game
    game = Game()
    game.game_loop()

