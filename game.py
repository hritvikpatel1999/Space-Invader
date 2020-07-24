import pygame
import random
import math
#Initialize pygame: Very important!
pygame.init()
screen = pygame.display.set_mode((800,600), pygame.RESIZABLE)

start_background = pygame.image.load('background_space.jpg')





'''    
def starting_page():
    while 1:
        screen.fill((200, 0, 0))
        screen.blit(start_background, (0,0))
        x, y = pygame.mouse.get_pos()
        button1 = pygame.Rect(100, 260, 200, 50)
        pygame.draw.rect(screen, (255, 255, 255), button1, 6)
        
        if button1.collidepoint(x, y):
            if click:
                game()
                
        click = False;
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click =True
        pygame.display.update()
'''
    
#Game Loop -> Anythin you want to appear persistently needs to go inside while loop
#running=True
#def game():


#Change Title, Caption and Background color:
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background_space.jpg')



#Player:
playerImg = pygame.image.load('spaceship.png')
playerX=300
playerY=480
playerX_change = 0 


#Enemies:
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = [] 
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(40)


#Bullet:
bulletImg = pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready" #Ready state ->Can't see the bullet on screen; #Fire-> Bullet is on screen and moving



#Score:
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

#Game Over:
over_font = pygame.font.Font('freesansbold.ttf',64)

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow((enemyX-bulletX), 2))+(math.pow((enemyY-bulletY), 2)))
    if distance < 27:
        return True
    else:
        return False



while 1:
    screen.fill((200, 0, 0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()

# If keystroke is pressed check whether it is right or left.
        if event.type == pygame.KEYDOWN :  #KEYDOWN means key is pressed.
            #print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


#Setting player boundaries:    
    playerX+=playerX_change
    if playerX<0:
        playerX = 0
    if playerX>736:
        playerX = 736

#Enemy movement:
    for i in range(num_of_enemies):

        #Game Over:
        if enemyY[i]>440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000;
            game_over_text()
            break

        enemyX[i]+=enemyX_change[i]
        if enemyX[i] < 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        if enemyX[i] > 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]

#Collision:
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1

            enemyX[i]=random.randint(0, 735)
            enemyY[i]=random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

#Bullet Movement:
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY) #Screen is drawn first, player is over the screen
    show_score(textX, textY)

    #No update will happen coz not updated.
    pygame.display.update()
#starting_page()
#game()
