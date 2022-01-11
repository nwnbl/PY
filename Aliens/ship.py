import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('D:\VSCODECNM\PY\Aliens\ship1.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = (600,800)
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right == True and self.rect.right < 1200:
            self.rect.x += self.settings.ship_speed
        elif self.moving_left == True and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
        self.x = self.rect.x