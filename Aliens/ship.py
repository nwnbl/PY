import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('D:\VSCODECNM\PY\Aliens\ship1.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = (600,800)

        self.moving_right = False
        self.moving_left = False
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right == True:
            self.rect.x += 1
        elif self.moving_left == True:
            self.rect.x -= 1