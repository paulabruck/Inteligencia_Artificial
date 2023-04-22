import pygame

# load images
def load(image_path, size="default", convert="alpha", flip=False):
    if convert == "alpha":
        image = pygame.image.load(image_path).convert_alpha()
    else:
        image = pygame.image.load(image_path).convert()

    if flip:
        image = pygame.transform.flip(image, True, False)

    if size != "default":
        image = scale(image, size)

    return image

# scale images
def scale(image, size):
    return pygame.transform.smoothscale(image, size)

# draw images
def draw(surface, image, pos, pos_mode="top_left"):
    if pos_mode == "center":
        pos = list(pos)
        pos[0] -= image.get_width()//2
        pos[1] -= image.get_height()//2

    surface.blit(image, pos)

# draw stickers when game is over
def draw_stickers(surface,image,default_image_size, pos):
    image1 = load("Assets/harrys.png")
    image2 = load("Assets/castles.png")
   
    if image == "image1":
        image1 = pygame.transform.scale(image1, default_image_size)
        draw(surface, image1,pos ,pos_mode="center")
    elif image == "image2":
        image2 = pygame.transform.scale(image2, default_image_size)
        draw(surface, image2,pos ,pos_mode="center")
    
