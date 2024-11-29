import sys, pygame
from random import randint


# General Setup
pygame.init()

WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT) = (1280, 720)
display_surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

# Surface

player_surf = pygame.image.load("../images/player.png").convert_alpha()
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

    display_surface.blit(player_surf, (0, 0))
   
    pygame.display.flip()

    clock.tick(60)
