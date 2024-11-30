import sys, pygame
from random import randint


# General Setup
pygame.init()

WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT) = (1280, 720)
display_surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

# Surfaces

player_surf = pygame.image.load("../images/player.png").convert_alpha()
player_pos = [WINDOW_WIDTH / 2, WINDOW_HEIGHT/ 2]
player_rect = player_surf.get_frect(center = player_pos)
# player_dir = pygame.math.Vector2(-1, -1)
# player_speed = 1000

meteor_surf = pygame.image.load("../images/meteor.png").convert_alpha()
meteor_pos = [WINDOW_WIDTH / 2, WINDOW_HEIGHT/ 2]
meteor_rect = meteor_surf.get_frect(center = meteor_pos)

laser_surf = pygame.image.load("../images/laser.png").convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))

star = pygame.image.load("../images/star.png").convert_alpha()
star_pos = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(20)]


while True:
    dt = clock.tick(60) / 1000

    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.KEYDOWN:
        #     print(event.key)
        # if event.type == pygame.MOUSEMOTION:
        #     player_rect.center = event.pos

    # Player input
    player_rect.center = pygame.mouse.get_pos()

    # Draw the game
    display_surface.fill("darkgray")
    
    for pos in star_pos:
        display_surface.blit(star, pos)
    
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)
    display_surface.blit(player_surf, player_rect)


    # player_rect.center += player_dir * player_speed * dt

    pygame.display.flip()

