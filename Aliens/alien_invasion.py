import sys
import pygame

class AlienInvasion:
    """游戏资源管理+行为管理"""
    def __init__(self):
        """游戏初始化"""
        pygame.init()
        # 像素
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        """主循环"""
        while True:
            # 键盘鼠标事件监视
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 让最近绘制的屏幕可见
            pygame.display.flip()

if __name__ == "__main__":
    # 创建游戏实例
    ai = AlienInvasion()
    ai.run_game()