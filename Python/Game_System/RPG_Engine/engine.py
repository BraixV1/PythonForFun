"""Classes for characters."""


import sys, pygame
pygame.init()










size = width, height = 1920, 1080
speed = [1, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("Game_System\RPG_Engine\original.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    #if pygame.key.get_pressed[K_w] is True:
    #   ballrect = ballrect.move
        
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()