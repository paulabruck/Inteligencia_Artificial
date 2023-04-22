import pygame
import time
import random
from settings import *
from background import GameBackground
from hand import Hand
from hand_tracking import HandTracking
from snitch import Snitch
from bludger import Bludger
import cv2
import ui
import settings
import image
from menu import Menu

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = GameBackground()

        # Load camera
        self.cap = cv2.VideoCapture(0)

        self.sounds = {}
        self.sounds["catched"] = pygame.mixer.Sound("Assets/Sounds/i.mp3")
        self.sounds["catched"].set_volume(SOUNDS_VOLUME)
        self.sounds["screaming"] = pygame.mixer.Sound(f"Assets/Sounds/screaming.wav")
        self.sounds["screaming"].set_volume(SOUNDS_VOLUME)

    # reset all the needed variables
    def reset(self): 
        self.hand_tracking = HandTracking()
        self.hand = Hand()
        self.balls = []
        self.balls_catch_timer = 0
        self.score = 0
        self.game_start_time = time.time()

    # adds snitchs and bludgers to the game              
    def catch_balls(self):
        time_ = time.time()
        if time_ > self.balls_catch_timer:
            self.balls_catch_timer = time_ + SNITCH_CATCH_TIME

            # increase the probability that the ball will be a bludger over time
            # increase from 0 to 50 during all the game 
            i = (GAME_DURATION-self.time_left)/GAME_DURATION * 100  / 2  
            if random.randint(0, 100) < i:
                self.balls.append(Bludger())
            else:
                self.balls.append(Snitch())

            # add other snitch after the half of the game
            if self.time_left < GAME_DURATION/2:
                self.balls.append(Snitch())

    # loads camera
    def load_camera(self):
        _, self.frame = self.cap.read()

    # sets hand position in game
    def set_hand_position(self):
        self.frame = self.hand_tracking.scan_hands(self.frame)
        (x, y) = self.hand_tracking.get_hand_center()
        self.hand.rect.center = (x, y)

    # draws background , balls , score , time left 
    def draw(self):
        # draw the background
        self.background.draw(self.surface)
        # draw the balls
        for ball in self.balls:
            ball.draw(self.surface)
        # draw the hand
        self.hand.draw(self.surface)
        # draw the score
        ui.draw_text(self.surface, f"Score : {self.score}", (SCREEN_WIDTH//4, 5), COLORS["score"], font=FONTS["medium"],
                    shadow=True, shadow_color=(255,255,255))
        # draw the time left
        # change the text color if less than 5 seconds left
        timer_text_color = (160, 40, 0) if self.time_left < 5 else COLORS["timer"] 
        ui.draw_text(self.surface, f"Time left : {self.time_left}", (SCREEN_WIDTH//2, 5),  timer_text_color, font=FONTS["medium"],shadow=True, shadow_color=(255,255,255))

    # updates time left of the game
    def game_time_update(self):
        self.time_left = max(round(GAME_DURATION - (time.time() - self.game_start_time), 1), 0)

    # loads camera, sets the hand in position , updates time and controls the catching of the balls
    def update(self):

        self.load_camera()
        self.set_hand_position()
        self.game_time_update()

        self.draw()

        if self.time_left > 0:
            self.catch_balls()
            (x, y) = self.hand_tracking.get_hand_center()
            self.hand.rect.center = (x, y)
            self.hand.left_click = self.hand_tracking.hand_closed
            print("Hand closed", self.hand.left_click)
            if self.hand.left_click:
                self.hand.image = self.hand.image_smaller.copy()
            else:
                self.hand.image = self.hand.original_image.copy()
            self.score = self.hand.catch_balls(self.balls, self.score, self.sounds)
            for ball in self.balls:
                ball.move()

        # when the game is over
        else: 
            Menu.show_game_over(self)
            if ui.button(self.surface, 500, "Continue", click_sound=self.sounds["catched"]):
                return "menu"


        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)
