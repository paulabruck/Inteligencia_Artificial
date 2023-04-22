import pygame

WINDOW_NAME = "Harry's Quiditch Practice"
GAME_TITLE = WINDOW_NAME

RULES = "GAME RULES"
GAME_RULES_ENGLISH = "\n\n\n QUIDITCH PRACTICE:  \n- In this game you get to be Harry Potter and have the chance to live an authentic quiditch practice at Hogwarts famous pitch. \n- Use your hand to control the game. Make sure your hand is between your cameras boundaries , your palm facing the front. Keep the hand extended , once you are close to the snitch close it to grab it and win points. Be careful with the BLUDGERS balls their task is to destabilize you from your broom, if you catch one of them you will lose points." 
GAME_RULES_SPANISH = "\n\n PRACTICA DE QUIDITCH:  \n- En este juego sentite como si eres Harry Potter y tienes la oportunidad de vivir una auténtica práctica de quiditch en el famoso campo de Hogwarts. \n- Usa tu mano para controlar el juego. Asegúrese de que su mano esté entre los límites de su cámara, con la palma hacia el frente. Mantenga la mano extendida, una vez que esté cerca de la snitch, ciérrela para agarrarla y ganar puntos. Ten cuidado con las pelotas BLUDGERS que intentan obstaculizarte tu tarea y desestabilizarte de tu escoba ,si atrapas una de ellas perderas puntos. " 
GAME_OVER= "GAME OVER"

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700

FPS = 90

# sizes
BUTTONS_SIZES = (240, 90)
HAND_SIZE = 200
HAND_HITBOX_SIZE = (60, 80)
SNITCH_SIZES = (50, 38)
# for each new snitch, it will multiply the size with an random value beteewn X and Y
SNITCH_SIZE_RANDOMIZE = (1,2) 
BLUDGERS_SIZES = (50, 50)
BLUDGER_SIZE_RANDOMIZE = (1.2, 1.5)

# drawing
# will draw all the hitbox
DRAW_HITBOX = False 

# animation
# the frame of the balls will change every X sec
ANIMATION_SPEED = 0.08

# difficulty
# the game will last X sec
GAME_DURATION = 60
SNITCH_CATCH_TIME = 1
SNITCH_MOVE_SPEED = {"min": 15, "max": 20}
# will remove X of the score of the player (if he catches a bludger)
BLUDGER_PENALITY = 300 

# colors
# second is the color when the mouse is on the button
COLORS = {"title": (56, 67, 209), "score": (38, 61, 39), "timer": (38, 61, 39),
            "buttons": {"default": (56, 67, 209), "second":  (87, 99, 255),
                        "text": (255, 255, 255), "shadow": (46, 54, 163)}} 

# sounds / music
# value between 0 and 1
MUSIC_VOLUME = 0.25 
SOUNDS_VOLUME = 1

# fonts
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 40)
FONTS["medium"] = pygame.font.Font(None, 72)
FONTS["big"] = pygame.font.Font(None, 120)
