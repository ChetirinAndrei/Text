import pygame

W = 800
M = 600

WHITE = (255, 255, 255)
YELLOW = (255, 230, 0)
BLUE = (0, 0, 51)

pygame.init()

pygame.display.set_caption('Text')
screen = pygame.display.set_mode((W, M))
pygame.mouse.set_visible(False)

font = pygame.font.SysFont('Arial', 60, True, False)
font2 = pygame.font.SysFont('Arial', 35, False, True)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False
    screen.fill(BLUE)
    screen.blit(font.render('Bceм привет', True, WHITE), (230, 200))
    screen.blit(font2.render('задание на урок', True, YELLOW), (270, 300))
    cube = pygame.Surface((50, 50))
    cube.fill((200, 0, 0))
    screen.blit(cube, (370, 100))
    if CW == 1:
        CM += 0.1
        
        

    pygame.display.update()
