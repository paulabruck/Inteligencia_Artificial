import pygame
import random
import image
from settings import *
from snitch import Snitch

class Bludger(Snitch):
    def __init__(self):
        #size
        random_size_value = random.uniform(BLUDGER_SIZE_RANDOMIZE[0], BLUDGER_SIZE_RANDOMIZE[1])
        size = (int(BLUDGERS_SIZES[0] * random_size_value), int(BLUDGERS_SIZES[1] * random_size_value))
        # moving
        moving_direction, start_pos = self.define_catch_pos(size)
        # sprite
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        # loading images
        self.images = [image.load(f"Assets/bludger/{i}.png", size=size, flip=moving_direction=="right") for i in range(1, 7)] 
        self.current_frame = 0
        self.animation_timer = 0
        
    # remove the bludger from the list
    def catch(self, bludger): 
        bludger.remove(self)
        return -BLUDGER_PENALITY
