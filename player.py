import pygame
from pygame import Rect, Color
from pygame.constants import K_LEFT, K_RIGHT

from pymunk import Body, Poly
import pymunk

from config import GRAVITY, WIDTH, HEIGHT


class Player:

    def __init__ (self, space):
        
        # size
        self.w = 25
        self.h = 25

        # position
        self.x = WIDTH // 2 - self.w // 2
        self.y = HEIGHT // 2 - self.h // 2

        # pygame rectangle
        self.rect = Rect (self.x, self.y, self.w, self.h)
        self.color = Color (209, 87, 0)

        # physics
        self.rigidbody = Body (0, 5, body_type=Body.DYNAMIC)
        self.rigidbody.position = self.x, self.y
        
        self.hitbox = pymunk.Circle (self.rigidbody, self.w / 2)
        self.hitbox.mass = 10
        self.hitbox.elasticity = 0
        self.hitbox.friction = 0

        space.add (self.rigidbody, self.hitbox)

        

    
    def update (self, dt):

        keys = pygame.key.get_pressed()

        if keys [K_LEFT] or keys [K_RIGHT]:

            if keys [K_LEFT]:
                self.rigidbody.apply_force_at_world_point ( (-1000,0), (0,0) )

            if keys [K_RIGHT]:
                self.rigidbody.apply_force_at_world_point ( (1000,0), (0,0) )




        x = int (self.rigidbody.position.x)
        y = int (self.rigidbody.position.y)
        self.x = x
        self.y = y
        self.rect.update(x, y, self.w, self.h)

        return



    def draw (self, window):
    
        pygame.draw.rect (window, self.color, self.rect)

        return