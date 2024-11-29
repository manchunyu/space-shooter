import os, sys, pygame
from random import randint


# General Setup
pygame.init()

WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT) = (1280, 720)
display_surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Space Shooter")

# Surface
surf = pygame.Surface((100, 200))
x = 50

player_surf = pygame.image.load(os.path.join("..", "images", "player.png")).convert_alpha()
star = pygame.image.load("../images/star.png").convert_alpha()
star_pos = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(20)]

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    display_surface.fill("darkgray")
    
    for pos in star_pos:
        display_surface.blit(star, pos)

    display_surface.blit(player_surf, (x,50))
    x += 0.01
    pygame.display.flip()
