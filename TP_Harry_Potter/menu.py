import pygame
import sys
from settings import *
from background import Background
import settings
import image
import ui

class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()
        self.click_sound = pygame.mixer.Sound(f"Assets/Sounds/i.mp3")

    # draw background and title
    def draw(self):
        self.background.draw(self.surface)
        # draw title
        ui.draw_text(self.surface, GAME_TITLE, (510, 50), COLORS["title"], font=FONTS["big"],
                    shadow=True, shadow_color=(255,255,255), pos_mode="center")
    
    # explains the game
    def show_rules(self):
        self.surface.fill((0,128,128))
        ui.draw_text( self.surface, settings.RULES, (600, 60), COLORS["title"], font=FONTS["big"],
        shadow=True, shadow_color=(255,255,255), pos_mode="center")
        ui.display_text(self.surface, settings.GAME_RULES_ENGLISH +settings.GAME_RULES_SPANISH, (20,20), settings.FONTS["small"], COLORS["title"],shadow=True, shadow_color=(255,255,255))
        
    # draws score , background and images when game is over
    def show_game_over(self):
        self.surface.fill((0,128,128))
        ui.draw_text( self.surface, settings.GAME_OVER, (600, 80), COLORS["title"], font=FONTS["big"],
        shadow=True, shadow_color=(255,255,255), pos_mode="center")
        ui.display_text(self.surface, f"Your Score is: {self.score}", (300,300), settings.FONTS["big"], COLORS["title"],shadow=True, shadow_color=(255,255,255))
        image.draw_stickers(self.surface, "image1" ,(128,320), (150, 220))
        image.draw_stickers(self.surface, "image2" ,(320, 152),(900, 540))
        image.draw_stickers(self.surface,"image3" ,(320, 152),(900, 540))

    # draw menu options start, rules and quit
    def update(self):
        self.draw()
        if ui.button(self.surface, BUTTONS_SIZES[1]*1.5, "START", click_sound=self.click_sound):
            return "game"
        
        if ui.button(self.surface, 150+BUTTONS_SIZES[1]*1.5, "RULES", click_sound=self.click_sound):
            return "rules"

        if ui.button(self.surface, 300+BUTTONS_SIZES[1]*1.5, "QUIT", click_sound=self.click_sound):
            pygame.quit()
            sys.exit()
  