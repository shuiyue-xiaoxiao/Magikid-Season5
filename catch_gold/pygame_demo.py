import pygame
from pygame.locals import *
import sys

pygame.init()  # 初始化

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch Gold")

gold_x, gold_y = 300, 30  # 金币中心点坐标
vel_y = 5  # 下落速度

# 主循环
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    # 金币下落
    gold_y += vel_y
    pygame.draw.circle(screen, (255, 255, 0), (gold_x, gold_y), 30)
    # 判断反弹
    if gold_y - 30 <= 0 or gold_y + 30 >= HEIGHT:  # 反弹条件
        vel_y = - vel_y  # 反弹

    pygame.display.update()  # 更新屏幕
    pygame.time.delay(10)  # 间隔时间
