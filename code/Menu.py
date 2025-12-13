#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_GREEN, MENU_OPTION, C_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuSpace000.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/SpaceSound000.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Space", C_GREEN, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Mage", C_GREEN, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_GREEN, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            # COMANDOS DO JOGO (CANTO SUPERIOR ESQUERDO)
            x = 20
            y = 20

            self.menu_text_left(18, "COMANDOS", C_GREEN, (x, y))

            self.menu_text_left(14, "Jogador 1", C_WHITE, (x, y + 25))
            self.menu_text_left(14, "Setas - Mover", C_WHITE, (x, y + 40))
            self.menu_text_left(14, "CTRL Direito - Atacar", C_WHITE, (x, y + 55))

            self.menu_text_left(14, "Jogador 2", C_WHITE, (x, y + 80))
            self.menu_text_left(14, "W, A, S, D - Mover", C_WHITE, (x, y + 95))
            self.menu_text_left(14, "CTRL Esquerdo - Atacar", C_WHITE, (x, y + 110))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def menu_text_left(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(topleft=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)