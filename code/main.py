import sys, pygame
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load("../images/player.png").convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT/ 2))
        self.speed = 300
        self.dir = pygame.math.Vector2()

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.dir.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.dir.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.dir = self.dir.normalize() if self.dir else self.dir
        self.rect.center += self.dir * self.speed * dt  

        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_SPACE]:
            print("FIRE!")
        
class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center=(randint(0, WINDOW_HEIGHT), randint(0, WINDOW_WIDTH)))
      

# General Setup
pygame.init()

WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT) = (1280, 720)
SCREEN_CENTER = [WINDOW_WIDTH / 2, WINDOW_HEIGHT/ 2]
display_surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

star_surf = pygame.image.load("../images/star.png").convert_alpha()
for _ in range(20):
    Star(all_sprites, star_surf)

player = Player(all_sprites)



# Surfaces
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
    
    # Update 
    all_sprites.update(dt)
    
    # Draw the game
    display_surface.fill("darkgray")
    
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)
    
    all_sprites.draw(display_surface)

    pygame.display.flip()

