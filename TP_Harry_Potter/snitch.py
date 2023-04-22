import pygame
import random
import time
import image
from settings import *

class Snitch:
    def __init__(self):
        #size
        random_size_value = random.uniform(SNITCH_SIZE_RANDOMIZE[0], SNITCH_SIZE_RANDOMIZE[1])
        size = (int(SNITCH_SIZES[0] * random_size_value), int(SNITCH_SIZES[1] * random_size_value))
        # moving
        moving_direction, start_pos = self.define_catch_pos(size)
        # sprite
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        self.images = [image.load("Assets/snitch/snitch.png", size=size, flip=moving_direction=="right")]
        self.current_frame = 0
        self.animation_timer = 0

    # define the start pos and moving vel of the snitch
    def define_catch_pos(self, size): 
        vel = random.uniform(SNITCH_MOVE_SPEED["min"], SNITCH_MOVE_SPEED["max"])
        moving_direction = random.choice(("left", "right", "up", "down"))
        if moving_direction == "right":
            start_pos = (-size[0], random.randint(size[1], SCREEN_HEIGHT-size[1]))
            self.vel = [vel, 5]
        if moving_direction == "left":
            start_pos = (SCREEN_WIDTH + size[0], random.randint(size[1], SCREEN_HEIGHT-size[1]))
            self.vel = [-vel, 5]
        if moving_direction == "up":
            start_pos = (random.randint(size[0], SCREEN_WIDTH-size[0]), SCREEN_HEIGHT+size[1])
            self.vel = [5, -vel]
        if moving_direction == "down":
            start_pos = (random.randint(size[0], SCREEN_WIDTH-size[0]), -size[1])
            self.vel = [5, vel]
        return moving_direction, start_pos

    # moves snitch
    def move(self):
        self.rect.move_ip(self.vel)

    # change the frame of the snitch when needed
    def animate(self): 
        time_ = time.time()
        if time_ > self.animation_timer:
            self.animation_timer = time_ + ANIMATION_SPEED
            self.current_frame += 1
            if self.current_frame > len(self.images)-1:
                self.current_frame = 0

    # draws rectangle
    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect)

    # draws snitch
    def draw(self, surface):
        self.animate()
        image.draw(surface, self.images[self.current_frame], self.rect.center, pos_mode="center")
        if DRAW_HITBOX:
            self.draw_hitbox(surface)

    # remove the snitch from the list
    def catch(self, snitch): 
        snitch.remove(self)
        return 150
