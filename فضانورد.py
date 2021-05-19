import pygame
import random
from pygame.locals import *
# وارد كردن كتابخانه

screen_height = 600
screen_width = 800
# اندازه صفحه

score = 0
level = 0
# مقدار دهی امتياز
fps = 120
clock = pygame.time.Clock()
# مقدار FPS

player_pos = [screen_width/2, screen_height/2]
player_speed = [0,0]
enemy_one_pos = [random.randint(0, screen_width-70),0]
enemy_two_pos = [0, random.randint(0, screen_width-70)]
astronaut_pos = [random.randint(0, screen_height-85) , random.randint(0, screen_width-70)]
# موقعيت

def move_player():
    screen.blit(player2, (player_pos[0], player_pos[1]))
    player_pos[0] += player_speed[0]
    player_pos[1] += player_speed[1]

    if player_pos[0] <= 0:
        player_pos[0] = screen_width-200
    elif player_pos[0] >= screen_width-200:
        player_pos[0] = 0
    if player_pos[1] <= 0:
        player_pos[1] = screen_height-200
    elif player_pos[1] >= screen_height-100:
        player_pos[1] = 0
# تابع حركت بازيكن
def move_enemy() :
    global score
    screen.blit(enemy2, (enemy_one_pos[0], enemy_one_pos[1]))
    screen.blit(enemy2, (enemy_two_pos[0], enemy_two_pos[1]))

    enemy_one_speed = random.randint(0, 5)
    enemy_two_speed = random.randint(0, 5)

    if 0 <= (enemy_one_pos[1]) <= (screen_height -70) :
        enemy_one_pos[1] += enemy_one_speed
    else :
        enemy_one_pos[1] = 0
        enemy_one_pos[0] = random.randint(0, screen_width-70)
        score += 1
    if 0 <= (enemy_two_pos[0]) <= (screen_width - 70):
        enemy_two_pos[0] += enemy_two_speed
    else :
        enemy_two_pos[0] = 0
        enemy_two_pos[1] = random.randint(0, screen_height-85)
        score += 1
# تابع حرکت دشمن
def check_collision(player,enemy) :
    player_x = player[0]
    player_y = player[1]
    enemy_x = enemy[0]
    enemy_y = enemy[1]
    if(player_x <= enemy_x < (player_x + 200)) or (enemy_x <= player_x <(enemy_x + 70)):
        if (player_y <= enemy_y < (player_y + 100)) or (enemy_y <= player_y < (enemy_y + 85)):
            return True
    else:
        return False
# تابع برخورد با دشمن
def creat_astronaut() :
    screen.blit(astronaut2, (astronaut_pos[0], astronaut_pos[1]))
    if check_collision(player_pos,astronaut_pos) :
        global score
        score+=5
        astronaut_pos[0] = random.randint(0, screen_width-70)
        astronaut_pos[1] = random.randint(0, screen_height-85)
# تابع حرکت فضانورد

pygame.init()
running = 1
# مقدار دهي اوليه (شروع شدن)

screen = pygame.display.set_mode((screen_width, screen_height))
# ساختن صفحه

background = pygame.image.load("space"+str(level)+".jpg")
player = pygame.image.load("ufo.png")
enemy = pygame.image.load("monster.png")
astronaut = pygame.image.load("astronaut.png")
# مقدار دهی عکس ها

background2 = pygame.transform.scale(background, (screen_width, screen_height))
player2 = pygame.transform.scale(player, (200 , 100))
enemy2 = pygame.transform.scale(enemy, (70, 85))
astronaut2 = pygame.transform.scale(astronaut, (70, 85))
# تغيير اندازه عکس ها

while running:
    if level<2:
        background = pygame.image.load("space"+str(level)+".jpg")
        background2 = pygame.transform.scale(background, (screen_width, screen_height))
    screen.blit(background2,(0,0))
    # رسم كردن پس زمينه

    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
            quit()
            # توقف بازی
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                player_speed[0] = 8
            if event.key == K_LEFT:
                player_speed[0] = -8
            if event.key == K_UP:
                player_speed[1] = -8
            if event.key == K_DOWN:
                player_speed[1] = 8
            # حركت با دكمه ها
        if event.type == KEYUP:
            player_speed = [0,0]
            # توقف با برداشتن دكمه ها
    # گرفتن رویداد ها

    if check_collision(player_pos, enemy_one_pos) == 1 or check_collision(player_pos, enemy_two_pos) == 1:
        background = pygame.image.load("game over.jpg")
        running = 0
        break
    # چک کردن برخورد با دشمن
    
    enemy_one_speed = random.randint(level, level+2)
    enemy_two_speed = random.randint(level, level+2)
    # سرعت نسیت به مرحله
    
    level = score//20
    # تنظیم مرحله
    
    creat_astronaut()
    move_enemy()
    move_player()
    clock.tick(fps)
    pygame.display.update()
    # اعمال كردن تغييرات
