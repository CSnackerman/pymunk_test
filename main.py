# 3rd party modules
import pygame
from pygame.locals import *

import pymunk

# my modules
from config import GRAVITY, WIDTH, HEIGHT
from player import Player
from ground import Ground


# setup pygame
pygame.init()
window = pygame.display.set_mode ((WIDTH, HEIGHT))
clock = pygame.time.Clock()
framerate = 60


# setup pymunk
space = pymunk.Space()
space.gravity = (0, GRAVITY)


# setup game objects
player = Player (space)
floor = Ground (space)

running = True
while running:

    # time
    clock.tick (framerate)
    dt = clock.get_time() / 1000.0

    # events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # update
    space.step (1.0 / framerate)
    player.update (dt)
    
    # erase
    window.fill ((50, 50, 255))

    # draw
    floor.draw (window)
    player.draw (window)
    

    # swap
    pygame.display.update()




pygame.quit()