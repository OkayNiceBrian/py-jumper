import sys
import pygame
from Jumper import Jumper
pygame.init()

size = width, height = 1280, 720
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

leftPressed = False
rightPressed = False
spacePressed = False

ball = pygame.image.load("assets/soccer-ball.png")
jumper = Jumper(0, height - 200)
ballrect = ball.get_rect(topleft=(jumper.x, jumper.y))

while 1:
    # Events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leftPressed = True
            if event.key == pygame.K_RIGHT:
                rightPressed = True
            if event.key == pygame.K_SPACE:
                spacePressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftPressed = False
            if event.key == pygame.K_RIGHT:
                rightPressed = False
            if event.key == pygame.K_SPACE:
                spacePressed = False

    # Update
    if leftPressed and rightPressed:
        jumper.stop()
    elif leftPressed:
        jumper.left()
    elif rightPressed:
        jumper.right()
    else:
        jumper.stop()

    if spacePressed:
        jumper.jump()

    jumper.update()

    ballrect.x = jumper.x
    ballrect.y = jumper.y

    if jumper.y >= height - 200:
        jumper.isJumping = False
        jumper.y = height - 200
        jumper.yspeed = 0

    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]

    # Draw
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
