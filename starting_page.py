import pygame
pygame.init()
screen = pygame.display.set_mode((800,600), pygame.RESIZABLE)

start_background = pygame.image.load('background_space.jpg')

#def play_text():
def game():
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load('spaceship.png')
    pygame.display.set_icon(icon)
    background = pygame.image.load('background_space.jpg')
    
    while 1:
        screen.fill((200, 0, 0))
#        screen.blit(background, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                
    pygame.display.update()
    
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
starting_page()

