import pygame
from settings import *

# draws text
def draw_text(surface, text, pos, color, font=FONTS["medium"], pos_mode="top_left",
                shadow=False, shadow_color=(0,0,0), shadow_offset=2):
    label = font.render(text, 1, color)
    label_rect = label.get_rect()
    if pos_mode == "top_left":
        label_rect.x, label_rect.y = pos
    elif pos_mode == "center":
        label_rect.center = pos
    # make the shadow
    if shadow: 
        label_shadow = font.render(text, 1, shadow_color)
        surface.blit(label_shadow, (label_rect.x - shadow_offset, label_rect.y + shadow_offset))
    # draw the text
    surface.blit(label, label_rect) 

# displays text with shadow and format
def display_text(surface, text, pos, font, color,shadow=False, shadow_color=(255,255,255), shadow_offset=2):
    collection = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    x,y = pos
    for lines in collection:
        for words in lines:
            word_surface = font.render(words, True, color)
            if shadow: 
                label_shadow = font.render(words, True, shadow_color)
            word_width , word_height = word_surface.get_size()

            if x + word_width >= 1200:
                x = pos[0]
                y += word_height
            surface.blit(label_shadow, (x - shadow_offset, y + shadow_offset))
            surface.blit(word_surface, (x,y))
            
            x += word_width + space
        x = pos[0]
        y += word_height
        
# draws buttons
def button(surface, pos_y, text=None, click_sound=None):
    rect = pygame.Rect((200 - BUTTONS_SIZES[0]//2, pos_y), BUTTONS_SIZES)

    on_button = False
    if rect.collidepoint(pygame.mouse.get_pos()):
        color = COLORS["buttons"]["second"]
        on_button = True
    else:
        color = COLORS["buttons"]["default"]
    # draw the shadow rectangle
    pygame.draw.rect(surface, COLORS["buttons"]["shadow"], (rect.x - 6, rect.y - 6, rect.w, rect.h)) 
    # draw the rectangle
    pygame.draw.rect(surface, color, rect) 
    # draw the text
    if text is not None:
        draw_text(surface, text, rect.center, COLORS["buttons"]["text"], pos_mode="center",
                    shadow=True, shadow_color=COLORS["buttons"]["shadow"])
    # if the user press on the button
    if on_button and pygame.mouse.get_pressed()[0]: 
        # play the sound if needed
        if click_sound is not None: 
            click_sound.play()
        return True
