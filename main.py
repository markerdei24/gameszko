import pygame

pygame.init()

#window
width = 800
height = width * 0.8

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Gameszkó')

#colors
bg_color = (185, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

#gravity
gravity = 0.75
player2_gravity = 0.75
#player1

alive = True

ammo = 20

x = 200
y = 200
player_img = pygame.image.load('./images/player1.png')
rect = player_img.get_rect()
rect.center = (x, y)

draw_player = window.blit(player_img, rect)

#player 2
player2_alive = True

player2_ammo = 20

player2_x = 400
player2_y = 400
player2_img = pygame.image.load('./images/player2.png')
player2_rect = player2_img.get_rect()
player2_rect.center = (player2_x, player2_y)

draw_player2 = window.blit(player2_img, player2_rect)

#player2 movement
player2_jump = False
player2_move_left = False
player2_move_right = False
player2_jump_block = False
player2_reload = False
player2_hit = False
player2_move_block = False

player2_kick_y = -5
player2_kick_x = 5

player2_kick_range = 0
player2_kick_height = 0

player2_speed = 5

player2_dx = 0
player2_dy = 0

player2_direction = 1
player2_shoot_direction = 1

player2_shoot_cooldown = 0

player2_reload_time = 0

player2_reload_start = width - 130
player2_reload_end = width - 5

player2_flip = True
player2_shoot = False

player2_jump_hight = 0

def player2_reload_animation():
    reload_line = pygame.draw.line(window, red, (player2_reload_start, 72), (player2_reload_end, 72))
#movement
jump = False
move_left = False
move_right = False
jump_block = False
reload = False
hit = False
move_block = False

kick_y = -5
kick_x = 5

kick_range = 0
kick_height = 0

speed = 5

dx = 0
dy = 0

direction = 1
shoot_direction = 1

shoot_cooldown = 0

reload_time = 0

reload_start = 70
reload_end = 205

def reload_animation():
    reload_line = pygame.draw.line(window, red, (reload_start, 72), (reload_end, 72))

flip = True

jump_hight = 0
#hp bar
hp_x = 150
hp_y = 20
hp = 7
life = 1
profile = 1
profile_x = 33
profile_y = 33
def hp_bar():
    hp_bar_img = pygame.image.load(f'./images/hp_bar{life}.jpg')
    hp_rect = hp_bar_img.get_rect()
    hp_rect.center = (hp_x, hp_y)
    draw_hp_bar = window.blit(hp_bar_img, hp_rect)
def profile_picture():
    profile_img = pygame.image.load(f'./images/player1_kep{profile}.png')
    profile_rect = profile_img.get_rect()
    profile_rect.center = (profile_x, profile_y)
    draw_profile = window.blit(profile_img, profile_rect)

#player2 hp bar
player2_hp_x = width - 85
player2_hp_y = 20
player2_hp = 7
player2_life = 1
def player2_hp_bar():
    player2_hp_bar_img = pygame.image.load(f'./images/player2_hp_bar{player2_life}.jpg')
    player2_hp_rect = player2_hp_bar_img.get_rect()
    player2_hp_rect.center = (player2_hp_x, player2_hp_y)
    player2_draw_hp_bar = window.blit(player2_hp_bar_img, player2_hp_rect)


#FPS set
clock = pygame.time.Clock()
fps = 60

def background():
    window.fill(bg_color)

#shoot
shoot = False

bullet_img =pygame.image.load('./images/bullet.png')

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, shoot_direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.shoot_direction = shoot_direction
    def update(self):
        self.rect.x += (self.speed * self.shoot_direction)
        if self.rect.right < width * -1 or self.rect.left > width * 2:
            self.kill()
        if self.rect.x == player2_rect.x or self.rect.x == player2_rect.x -1 or self.rect.x == player2_rect.x -2 or self.rect.x == player2_rect.x -3 or self.rect.x == player2_rect.x -4 or self.rect.x == player2_rect.x -5 or self.rect.x == player2_rect.x + 1 or self.rect.x == player2_rect.x + 2 or self.rect.x == player2_rect.x + 3 or self.rect.x == player2_rect.x + 4 or self.rect.x == player2_rect.x + 5 or self.rect.x == player2_rect.x -6 or self.rect.x == player2_rect.x -7 or self.rect.x == player2_rect.x -8 or self.rect.x == player2_rect.x -9 or self.rect.x == player2_rect.x -10 or self.rect.x == player2_rect.x + 6 or self.rect.x == player2_rect.x + 7 or self.rect.x == player2_rect.x + 8 or self.rect.x == player2_rect.x + 9 or self.rect.x == player2_rect.x + 10:
            if self.rect.y <= player2_rect.bottom and self.rect.y >= player2_rect.top - 10:
                self.kill()
                print('hit')
                if globals()['player2_life'] < 7:
                    globals()['player2_hit'] = True
                    if globals()['player2_hp'] != 1:
                        globals()['player2_hp'] -= 1

        if self.rect.x == rect.x or self.rect.x == rect.x -1 or self.rect.x == rect.x -2 or self.rect.x == rect.x -3 or self.rect.x == rect.x -4 or self.rect.x == rect.x -5 or self.rect.x == rect.x + 1 or self.rect.x == rect.x + 2 or self.rect.x == rect.x + 3 or self.rect.x == rect.x + 4 or self.rect.x == rect.x + 5 or self.rect.x == rect.x - 6 or self.rect.x == rect.x - 7 or self.rect.x == rect.x - 8 or self.rect.x == rect.x - 9 or self.rect.x == rect.x - 10 or self.rect.x == rect.x + 6 or self.rect.x == rect.x + 7 or self.rect.x == rect.x + 8 or self.rect.x == rect.x + 9 or self.rect.x == rect.x + 10:
            if self.rect.y <= rect.bottom and self.rect.y >= rect.top - 10:
                self.kill()
                print('hit')
                if globals()['life'] < 7: 
                    globals()['hit'] = True
                    globals()['hp'] -= 1
                    globals()['profile'] += 1
                    if globals()['profile'] > 7:
                            globals()['profile'] = 1
                            globals()['hp'] = 7
                            globals()['life'] += 1

bullet_group = pygame.sprite.Group()

#write on window
def write(text, center):
    font = pygame.font.Font('./font/Waffle Story.ttf', 24)
    write_ammo = font.render(text, True, red)
    text_rect = write_ammo.get_rect()
    text_rect.center = center
    window.blit(write_ammo, text_rect)

#run the program
run = True
while run:

    #refresh the screen
    pygame.display.update()

    #fps
    clock.tick(fps)

    #draw
    background()
    pygame.draw.line(window, red, (0, 400), (width, 400))

    hp_bar()
    player2_hp_bar()

    write(f'Ammo: {ammo}', (130, 50))
    write(f'Ammo: {player2_ammo}', (width - 68, 50))

    draw_player
    draw_player2

    bullet_group.update()
    bullet_group.draw(window)

    profile_picture()
    #movement
    if rect.left < 0:
        move_left = False
    if rect.right > width:
        move_right = False


    #inputs
    for event in pygame.event.get():
        #quit
        if event.type == pygame.QUIT:
            run = False

        #movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and jump_block == False:
                jump = True
            if event.key == pygame.K_a and move_block == False:
                move_left = True
            if event.key == pygame.K_t:
                shoot = True
            elif event.key == pygame.K_d and move_block == False:
                move_right = True
            if event.key == pygame.K_r and reload == False and ammo < 20:
                reload = True
            if event.key == pygame.K_UP and player2_jump_block == False:
                player2_jump = True
            if event.key == pygame.K_LEFT and player2_move_block == False:
                player2_move_left = True
            if event.key == pygame.K_o:
                player2_shoot = True
            elif event.key == pygame.K_RIGHT and player2_move_block == False:
                player2_move_right = True
            if event.key == pygame.K_p and player2_reload == False and player2_ammo < 20:
                player2_reload = True 

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            elif event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_t:
                shoot = False
            if event.key == pygame.K_LEFT:
                player2_move_left = False
            elif event.key == pygame.K_RIGHT:
                player2_move_right = False
            if event.key == pygame.K_o:
                player2_shoot = False
    #player1 movement
    if hit:
        kick_range = kick_x * bullet.shoot_direction
        jump_hight = kick_y
        kick_x = kick_x * 1.2
        kick_y = kick_y - 1.3
        jump_block = True
        move_left = False
        move_right = False
        move_block = True
        hit = False
    if hp == 1:
        kick_x = 100
    if hp == 7:
        kick_x = 5
        kick_y = -5

    dx += kick_range
    
    if rect.bottom == 400:
        dx = 0

    if jump:
        jump_hight = -11
        jump = False
        jump_block = True
        
    jump_hight += gravity
    if jump_hight > 10:
        jump_hight
    dy += jump_hight
    
    if rect.bottom + dy > 400:
        dy = 400 - rect.bottom
        jump_block = False
        kick_range = 0
        move_block = False

    rect.x += dx
    rect.y += dy

    if move_left:
        dx += speed
        rect.x -= dx
        direction = -0.02
        shoot_direction = -1
        flip = False
    if move_right:
        dx += speed
        rect.x += dx
        direction = 1
        shoot_direction = 1
        flip = True
    if shoot and shoot_cooldown == 0 and ammo > 0 and reload == False:
        bullet = Bullet(rect.x + 60 * direction, rect.y + 50, direction, shoot_direction)
        bullet_group.add(bullet)
        shoot_cooldown = 20
        ammo -= 1

    if shoot_cooldown > 0:
        shoot_cooldown -= 1  

    if reload:
        reload_time += 1
        reload_animation()
        reload_end -= 0.81
    if reload_time == 150 and reload:
        ammo = 20
        reload = False
        reload_time = 0
        reload_end = 130

#player2 movement
    if player2_hit:
        player2_kick_range = player2_kick_x * bullet.shoot_direction
        player2_jump_hight = player2_kick_y
        player2_kick_x = player2_kick_x * 1.2
        player2_kick_y = player2_kick_y - 1.3
        player2_jump_block = True
        player2_move_left = False
        player2_move_right = False
        player2_move_block = True
        player2_hit = False
    if player2_hp == 1:
        player2_kick_x = 100

    player2_dx += player2_kick_range
    
    if player2_rect.bottom == 400:
        player2_dx = 0

    if player2_jump:
        player2_jump_hight = -11
        player2_jump = False
        player2_jump_block = True
        
    player2_jump_hight += player2_gravity
    player2_dy += player2_jump_hight
    
    if player2_rect.bottom + player2_dy > 400:
        player2_dy = 400 - player2_rect.bottom
        player2_jump_block = False
        player2_move_block = False
        player2_kick_range = 0

    player2_rect.x += player2_dx
    player2_rect.y += player2_dy

    if player2_move_left and player2_x < 0:
        player2_dx += player2_speed
        player2_rect.x -= player2_dx
        player2_direction = -0.02
        player2_shoot_direction = -1
        player2_flip = False
    if player2_move_right:
        player2_dx += player2_speed
        player2_rect.x += player2_dx
        player2_direction = 1
        player2_shoot_direction = 1
        player2_flip = True
        
    if player2_rect.x <= 0:
        player2_move_left = False
    elif player2_rect.x >= 755:
        player2_move_right = False

    if player2_shoot and player2_shoot_cooldown == 0 and player2_ammo > 0 and player2_reload == False:
        bullet = Bullet(player2_rect.x + 65 * player2_direction, player2_rect.y + 45, player2_direction, player2_shoot_direction)
        bullet_group.add(bullet)
        player2_shoot_cooldown = 20
        player2_ammo -= 1

    if player2_shoot_cooldown > 0:
        player2_shoot_cooldown -= 1  

    if player2_reload:
        player2_reload_time += 1
        player2_reload_animation()
        player2_reload_end -= 0.81
    if player2_reload_time == 150 and player2_reload:
        player2_ammo = 20
        player2_reload = False
        player2_reload_time = 0
        player2_reload_end = width - 5

    #turn
    if flip == True:
        draw_player = window.blit(pygame.transform.flip(player_img, flip, False), rect)
    else:
        draw_player = window.blit(pygame.transform.flip(player_img, flip, False), rect)

    if player2_flip == True:
        draw_player2 = window.blit(pygame.transform.flip(player2_img, player2_flip, False), player2_rect)
    else:
        draw_player2 = window.blit(pygame.transform.flip(player2_img, player2_flip, False), player2_rect)

    dx = 0
    dy = 0

    player2_dx = 0
    player2_dy = 0

#shut up the program
pygame.quit()