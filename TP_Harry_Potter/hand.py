import pygame
import image
from settings import *
from hand_tracking import HandTracking
import cv2

class Hand:
    def __init__(self):
        self.original_image = image.load("Assets/hand1.png", size=(HAND_SIZE, HAND_SIZE))
        self.image = self.original_image.copy()
        self.image_smaller = image.load("Assets/hand1.png", size=(HAND_SIZE - 50, HAND_SIZE - 50))
        self.rect = pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, HAND_HITBOX_SIZE[0], HAND_HITBOX_SIZE[1])
        self.left_click = False

    # change the hand position center at the mouse position
    def follow_mouse(self):
        self.rect.center = pygame.mouse.get_pos()

    # follows hand
    def follow_mediapipe_hand(self, x, y):
        self.rect.center = (x, y)

    # draws the hittable space 
    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect)

    # draws the hand
    def draw(self, surface):
        image.draw(surface, self.image, self.rect.center, pos_mode="center")

        if DRAW_HITBOX:
            self.draw_hitbox(surface)

    # return a list with all balls that collide with the hand hitbox
    def on_ball(self, balls): 
        return [ball for ball in balls if self.rect.colliderect(ball.rect)]

    # will catch the balls that collide with the hand when the left mouse button is pressed
    def catch_balls(self, balls, score, sounds): 
        # if left click
        if self.left_click: 
            for ball in self.on_ball(balls):
                ball_score = ball.catch(balls)
                score += ball_score
                
                if ball_score < 0:
                    sounds["screaming"].play()
                else: sounds["catched"].play()
        else:
            self.left_click = False
        return score
