import sys
import pygame
from settings import *
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """游戏资源管理+行为管理"""
    def __init__(self):
        """游戏初始化"""
        pygame.init()
        self.settings=Setting()
        # 像素
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color=self.settings.bg_color
        self.ship=Ship(self)
        self.bullets = pygame.sprite.Group()
    
    def run_game(self):
        """主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.bullets.update()
    
    def _check_events(self):
        # 键盘鼠标事件监视
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            
    
    def _update_screen(self):
        # 让最近绘制的屏幕可见
        pygame.display.flip()
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    
        

if __name__ == "__main__":
    # 创建游戏实例
    ai = AlienInvasion()
    ai.run_game()
