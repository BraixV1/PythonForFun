"""_This first test of module pygame."""

import sys, pygame

pygame.init()

size = width, height = 1920, 1080
speed = [2, 2]
black = 0, 0, 0


screen = pygame.display.set_mode(size)

ball = pygame.image.load("Pygame_projects\Project_001\intro_ball.gif")
ballrect = ball.get_rect()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()            #get a pygame clock object
player = pygame.image.load('Pygame_projects\Project_001\intro_ball.gif').convert()
entity = pygame.image.load('Pygame_projects\Project_001\intro_ball.gif').convert()
background = pygame.image.load('"C:\Users\Brajan\Downloads\pfp\$LOTHBOI+-+SPIRALING+Thumbnail+(SW).jpg"').convert()
screen.blit(background, (0, 0))
objects = []
p = GameObject(player, 10, 3)          #create the player object
for x in range(10):                    #create 10 objects</i>
    o = GameObject(entity, x*40, x)
    objects.append(o)
while True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        p.move(up=True)
    if keys[pygame.K_DOWN]:
        p.move(down=True)
    if keys[pygame.K_LEFT]:
        p.move(left=True)
    if keys[pygame.K_RIGHT]:
        p.move(right=True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    for o in objects:
        screen.blit(background, o.pos, o.pos)
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)
    pygame.display.update()
    clock.tick(60)


