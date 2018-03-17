import pygame
from pygame.locals import *
import random
import time

class BasePlane(object):
    def __init__(self, screen_temp, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)
        self.bullets_list = []
    def display(self):
        self.screen.blit(self.image,(self.x, self.y))
        for bullet in self.bullets_list:
            bullet.move()
            bullet.display()
            if bullet.judge():
                self.bullets_list.remove(bullet)

class BaseBullet(object):
    def __init__(self, x, y, screen_temp, image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

class HeroPlane(BasePlane):
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 210, 500, './feiji/hero1.png')

    def move_left(self):
        self.x -= 5
    def move_right(self):
        self.x += 5
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def fire(self):
        self.bullets_list.append(HeroBullet(self.screen, self))

    


class HeroBullet(BaseBullet):
    def __init__(self, screen_temp, hero_temp):
        BaseBullet.__init__(self, hero_temp.get_x() + 40, hero_temp.get_y() - 20, screen_temp, './feiji/bullet.png')

    def move(self):
        self.y -= 5
    def judge(self):
        if self.y < 0:
            return True
        else:
            return False
    


    
class EnemyPlane(BasePlane):
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, random.randint(0, 477), 0, './feiji/enemy0.png')
        self.direction = 'right'
    def move(self):
        if self.direction == 'right':
            self.x += 5
            if self.x >= 427:
                self.direction = 'left'
        elif self.direction == 'left':
            self.x -= 5
            if self.x <= 0:
                self.direction = 'right'
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y   
    def fire(self):
        random_num = random.randint(0, 100)
        if random_num == 3 or random_num == 8:
            self.bullets_list.append(EnemyBullet(self.screen, self))

    

class EnemyBullet(BaseBullet):
    def __init__(self, screen_temp, enemy_temp):
        BaseBullet.__init__(self, enemy_temp.get_x() + 20, enemy_temp.get_y() + 20, screen_temp, './feiji/bullet1.png')
        
    def move(self):
        self.y += 5
    def judge(self):
        if self.y > 660:
            return True
        else:
            return False
    

def key_control(hero_temp, enemy_temp):
    for event in pygame.event.get():
        #判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        #判断是否是按下了键
        elif event.type == KEYDOWN:
            #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()
            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            #检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()
                enemy_temp.fire()
                
def main():
    #创建窗口
    screen = pygame.display.set_mode((477, 660), 0, 32)
    #载入背景
    background = pygame.image.load('./feiji/background.png')
    #创建飞机
    hero = HeroPlane(screen)
    #创建敌机
    enemy = EnemyPlane(screen)
    
    while True:
        
        screen.blit(background,(0, 0))
        hero.display() 
        enemy.display()
        enemy.move()
        enemy.fire()
        pygame.display.update()
        key_control(hero, enemy)
        time.sleep(0.01)
#if __name__ == '__main':
main()