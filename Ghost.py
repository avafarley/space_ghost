import pygame

class Ghost(pygame.sprite.Sprite):
    def __init__(self, initial_y, initial_x):

        self.PLAYER_VEL = 15
        self.STAR_VEL = 3

        super().__init__()
        self.image = pygame.image.load("Assets\Sprites\RedGhost.png")
        self.rect = self.image.get_rect()
        self.rect.y = initial_y
        self.rect.x =

    while run:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - self.PLAYER_VEL >= -10:
            player.x -= self.PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + self.PLAYER_VEL + player.width <= self.WIDTH:
            player.x += self.PLAYER_VEL
        if keys[pygame.K_UP] and player.y + self.PLAYER_VEL >= 10:
            player.y -= self.PLAYER_VEL
        if keys[pygame.K_DOWN] and player.y + self.PLAYER_VEL + player.height <= self.HEIGHT:
            player.y += self.PLAYER_VEL


    def update(self):
        self.rect.x += 1