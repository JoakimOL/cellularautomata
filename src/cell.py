import pygame
import logging
import random

from enum import Enum

class Cell:
    def __init__(self, x, y, cellsize = 50, font = None):
        self.logger = logging.getLogger()
        self.SIZE = cellsize
        self.x = x
        self.y = y
        self.color = (255,255,255)
        self.new_color = self.color
        self.changed = False
        self.neighbours = []
        self.font = font
        self.texts = {}
    
    def __str__(self):
        return f"({self.x},{self.y}) = {self.color}"

    def draw(self, surface_to_draw_on):
        self.logger.debug(f"drawing at ({self.x},{self.y}). color = {self.color}")
        rect = pygame.draw.rect(surface_to_draw_on, self.color, (self.x*self.SIZE, self.y*self.SIZE, self.SIZE, self.SIZE))
        if(not self.font is None):
            if(not self.color in self.texts):
                self.texts[self.color] = self.font.render(str(self.color), True, (0,0,0))
            surface_to_draw_on.blit(self.texts[self.color], (self.x*self.SIZE, self.y*self.SIZE))

    def apply_rule(self):
        self.logger.warn("calling apply_rule on baseclass Cell")

    def commit_color(self):
        self.logger.warn("calling commit color on baseclass Cell")

class Simple_Cell(Cell):
    def __init__(self,x,y,initial_color,cellsize,font):
        super().__init__(x,y,cellsize,font)
        self.color = initial_color
        self.new_color = initial_color

    def apply_rule(self):
        random_neighbour = self.neighbours[random.randint(0,len(self.neighbours)-1)]

        if random_neighbour.color == self.color:
            return
        else:
            self.new_color = random_neighbour.color
            self.changed = True

    def commit_color(self):
        if(self.changed):
            self.logger.debug(f"changing color from {self.color} to {self.new_color}")
            self.color = self.new_color
            self.changed = False
            return True
        return False

