import sys
import pygame
from settings import *
from ship import Ship

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
    
    def run_game(self):
        """主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
    
    def _check_events(self):
        # 键盘鼠标事件监视
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
    
    def _update_screen(self):
        # 让最近绘制的屏幕可见
        pygame.display.flip()
        self.screen.fill(self.bg_color)
        self.ship.blitme()
    
        

if __name__ == "__main__":
    # 创建游戏实例
    ai = AlienInvasion()
    ai.run_game()
