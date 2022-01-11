import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """外星人"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        
        self.image = pygame.image.load(r'D:\VSCODECNM\PY\Aliens\ufo2.bmp')
        self.rect = self.image.get_rect()

        #self.rect.x = 400
        #self.rect.y = 600
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
