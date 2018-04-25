import sys
import pygame
from bullet import Bullet



def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """相应键盘按下"""
    if event.key==pygame.K_RIGHT: #向右移动飞船                      
        ship.moving_right=True
    if event.key==pygame.K_LEFT:#向左移动飞船          
       ship.moving_left=True
    if event.key==pygame.K_SPACE:#按下空格，发射子弹
        fire_bullet(ai_settings, screen, ship, bullets)   
    if event.key==pygame.K_q:  #按Q退出游戏
        sys.exit()

def check_keyup_events(event,ship):
    """相应键盘松开"""
    if event.key==pygame.K_RIGHT: #停止向右移动飞船                   
        ship.moving_right=False
    if event.key==pygame.K_LEFT: #停止向左移动飞船        
        ship.moving_left=False

def check_events(ai_settings,screen,ship,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)   

def update_screen(ai_settings,screen,ship,alien,bullets):
    """重绘屏幕"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets)<ai_settings.bullets_allowed:
        #创建一刻子弹，将其加入编组bullets中
        new_bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def update_bullets(bullets):
    bullets.update() #对编组中的所有子弹更新
    for bullet in bullets.copy():#删除消失的子弹
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
       # print(len(bullets))