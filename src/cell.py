import pygame
import logging
import random

from enum import Enum

class Cell:
    def __init__(self, x, y, initial_color = pygame.Color(255,0,0), cellsize = 50, font = None):
        self.logger = logging.getLogger()
        self.SIZE = cellsize
        self.x = x
        self.y = y
        self.color = initial_color
        self.new_color = initial_color
        self.changed = False
        self.neighbours = []
        self.initialized = False
        self.font = font
        self.text = None
    
    def is_initialized():
        return self.initialized

    def __str__(self):
        return f"({self.x},{self.y}) = {self.color}"

    def draw(self, surface_to_draw_on):
        self.logger.debug(f"drawing at ({self.x},{self.y}). color = {self.color}")
        rect = pygame.draw.rect(surface_to_draw_on, self.color, (self.x*self.SIZE, self.y*self.SIZE, self.SIZE, self.SIZE))
        if(not self.font is None):
            if(self.text is None):
                self.text = self.font.render(str(self.color), True, (255,255,255))
            surface_to_draw_on.blit(self.text, (self.x*self.SIZE, self.y*self.SIZE))

    def apply_rule(self):
        random_neighbour = self.neighbours[random.randint(0,len(self.neighbours)-1)]

        # random_neighbour = self.neighbours[0]
        if random_neighbour.color == self.color:
            return
        elif self.color == (255,0,0) and random_neighbour.color == (0,255,0):
            self.new_color = (0,255,0)
            self.changed = True
        elif self.color == (0,255,0) and random_neighbour.color == (0,0,255):
            self.new_color = (0,0,255)
            self.changed = True
        elif self.color == (0,0,255) and random_neighbour.color == (255,0,0):
            self.new_color = (255,0,0)
            self.changed = True
        # rød - stein
        # blå - saks
        # grønn - papir
        # if random_neighbour.color != self.color:
        #     self.new_color = random_neighbour.color
        #     self.changed = True
        # for neighbour in self.neighbours:
        #     if(neighbour.color == (0,0,0)):
        #         self.changed = True
        #         self.new_color = (0,0,0)
    def commit_color(self):
        if(self.changed):
            self.logger.debug(f"changing color from {self.color} to {self.new_color}")
            self.color = self.new_color
            self.changed = False
            return True
        return False

class RPS_Cell(Cell):
    class Kind(Enum):
        ROCK = 0
        PAPER = 1
        SCISSORS = 2
    
    def __init__(self, x, y, kind, initial_color = pygame.Color(255,0,0), cellsize = 50):
        super.__init__(x,y,initial_color, cellsize)
        self.kind = kind

    def apply_rule(self):
        random_neighbour = self.neighbours[random.randint(0,len(self.neighbours))]
        
