import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('D:\VSCODECNM\PY\Aliens\ship1.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = (600,800)
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)