import pygame
from pygame import Rect, Color

from pymunk import Body, Poly

from config import WIDTH, HEIGHT

class Ground:

    def __init__ (self, space):
        
        # size
        self.w = WIDTH - 20
        self.h = 25

        # position
        self.x = 10
        self.y = HEIGHT - self.h

        # pygame rectangle
        self.rect = Rect (self.x, self.y, self.w, self.h)
        self.color = Color (100, 6, 107)

        # physics
        self.rigidbody = Body (body_type=Body.STATIC)
        self.rigidbody.position = self.x + self.w / 2, self.y

        self.hitbox = Poly.create_box (self.rigidbody, (self.w, self.h))
        self.hitbox.elasticity = 0
        self.hitbox.mass = 1
        self.hitbox.friction = 0

        space.add (self.rigidbody, self.hitbox)


    def update (self, dt):
        return



    def draw (self, window):
        
        pygame.draw.rect (window, self.color, self.rect)

        return