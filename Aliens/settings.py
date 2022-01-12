from pygame.mouse import set_visible


class Setting:
    def __init__(self):
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color=(230,230,230)

        #飞船设置
        #self.ship_speed = 1.5
        self.ship_limit = 3

        #子弹设置
        #self.bullet_speed = 1.0
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (100,100,100)
        self.bullet_allowed = 5

        #外星人设置
        #self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #self.fleet_direction = 1    # 1 for right; -1 for left

        #加快节奏
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    
    #####################
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 50
    
    #####################
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
    
        self.alien_points = int(self.alien_points * self.score_scale) 