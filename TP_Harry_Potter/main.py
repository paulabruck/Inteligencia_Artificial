# Setup Python ----------------------------------------------- #
import pygame
import sys
from settings import *
from game import Game
from menu import Menu
import ui

# Setup pygame/window --------------------------------------------- #
pygame.init()
pygame.display.set_caption(WINDOW_NAME)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32)

mainClock = pygame.time.Clock()

# Fonts ----------------------------------------------------------- #
fps_font = pygame.font.SysFont("coopbl", 22)

# Music ----------------------------------------------------------- #
pygame.mixer.music.load("Assets/Sounds/music.mp3")
pygame.mixer.music.set_volume(MUSIC_VOLUME)
pygame.mixer.music.play(-1)

# Variables ------------------------------------------------------- #
state = "menu"

# Creation -------------------------------------------------------- #
game = Game(SCREEN)
menu = Menu(SCREEN)

# Functions ------------------------------------------------------ #
def user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

# update state of game
def update():
    global state
    if state == "menu":
        if menu.update() == "game":
            # reset the game to start a new game
            game.reset() 
            state = "game"
    if state == "menu":
        if menu.update() == "rules":
            menu.show_rules()
            state = "rules"
    elif state == "rules":
        if ui.button(SCREEN, 580, "Continue",  click_sound=None):
            state = "menu"
    elif state == "game":
        if game.update() == "menu":
            state = "menu"
    
    pygame.display.update()
    mainClock.tick(FPS)


# Loop ------------------------------------------------------------ #
while True:

    # Buttons ----------------------------------------------------- #
    user_events()

    # Update ------------------------------------------------------ #
    update()

    
