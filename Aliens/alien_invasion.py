import sys
import pygame
from settings import *
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats

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
        self.stats = GameStats(self)
        self.ship=Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
    
    #############
    def run_game(self):
        """主循环"""
        while True:
            self._check_events()

            if self.stats.game_active == True:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()
            # print(len(self.bullets))
    
    #############
    def _check_events(self):
        # 键盘鼠标事件监视
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            
    #############
    def _update_screen(self):
        # 让最近绘制的屏幕可见
        pygame.display.flip()
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

    #############
    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    ############
    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    #############
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    #############
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    #############
    def _create_fleet(self):
        alien = Alien(self)
        # 计算可以放多少个
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        available_space_x = self.settings.screen_width - 2 * alien_width
        available_space_y = self.settings.screen_height - 3 * alien_height - self.ship.rect.height
        available_number_alien_x = available_space_x // (2 * alien_width)
        available_number_alien_y = available_space_y // (2 * alien_height)

        for num_y in range(0, available_number_alien_y):
            for num_x in range(0, available_number_alien_x):
                self._create_alien(num_x, num_y)
    
    #############
    def _create_alien(self, num_x, num_y):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + 2 * alien_width * num_x
        alien.y = alien_height + 2 * alien_height * num_y
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)
    
    ############
    """在此处进行对碰撞判断和处理函数的调用"""
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        self._check_alien_bottom()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            #print("Ship hit!!!")
            self._ship_hit()

    #############
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    ############
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    ###########
    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.stats.game_active = False
    
    ############
    def _check_alien_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    
        
########################################################
if __name__ == "__main__":
    # 创建游戏实例
    ai = AlienInvasion()
    ai.run_game()
