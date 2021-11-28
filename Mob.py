import pygame
from Object import Object 
from pygame.math import Vector2
from Effect import Boom
import math

class Mob(Object):
    def __init__(self, img_path, size, velocity, missile):
        super().__init__(img_path, size, velocity)
        self.missile = missile
        self.is_targeted = False
        self.direction = Vector2(1,1)
        self.rad = 1

    def move(self, boundary, game):
        if (game.size[0] != self.boundary[0]) or (game.size[1] != self.boundary[1]): #update when screen resized
            self.on_resize(game.size)

        self.x += self.direction.y
        self.y += self.direction.x
        self.rad+=0.08*self.velocity
        self.direction.from_polar((self.velocity*4,math.sin(self.rad)*90))

        if self.y >= boundary[1] - self.sy:
            game.mobList.remove(self)

    def destroy(self, game):
        boom = Boom()
        mob_location = {"x":self.x+(self.sx/2), "y":self.y+(self.sy/2)}
        boom.set_XY((mob_location["x"] - boom.sx/2, mob_location["y"]- boom.sy/2))
        game.effect_list.append(boom)
        if self in game.mobList:
            game.mobList.remove(self)
                        

        