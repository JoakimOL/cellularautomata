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
        self.initialized = False
        self.font = font
        self.texts = {}
    
    def is_initialized():
        return self.initialized

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
        # random_neighbour = self.neighbours[random.randint(0,len(self.neighbours)-1)]

        # if random_neighbour.color == self.color:
        #     return
        # else:
        #     self.new_color = random_neighbour.color
        #     self.changed = True
        # if random_neighbour.color == self.color:
        #     return
        # elif self.color == (255,255,255):
        #     self.new_color = random_neighbour.color
        #     self.changed = True
        # elif self.color == (255,0,0) and random_neighbour.color == (0,255,0):
        #     self.new_color = (0,255,0)
        #     self.changed = True
        # elif self.color == (0,255,0) and random_neighbour.color == (0,0,255):
        #     self.new_color = (0,0,255)
        #     self.changed = True
        # elif self.color == (0,0,255) and random_neighbour.color == (255,0,0):
        #     self.new_color = (255,0,0)
        #     self.changed = True

    def commit_color(self):
        self.logger.warn("calling commit color on baseclass Cell")
        # if(self.changed):
        #     self.logger.debug(f"changing color from {self.color} to {self.new_color}")
        #     self.color = self.new_color
        #     self.changed = False
        #     return True
        # return False

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

class RPS_Cell(Cell):
    class Kind(Enum):
        ROCK = 0
        PAPER = 1
        SCISSORS = 2
        WALL = 3
        EMPTY = 4

    KIND_COLORS = {
        Kind.ROCK: (255,0,0),
        Kind.PAPER: (0,255,0),
        Kind.SCISSORS: (0,0,255),
        Kind.WALL: (0,0,0),
        Kind.EMPTY: (255,255,255)
    }
    
    def __init__(self, x, y, kind = Kind.EMPTY, cellsize = 50, font = None):
        super().__init__(x,y, cellsize, font)
        self.kind = kind
        self.color = self.KIND_COLORS[self.kind]

    def apply_rule(self):
        random_neighbour = self.neighbours[random.randint(0,len(self.neighbours))-1]
        if random_neighbour.kind == self.kind:
            return
        elif self.kind == self.Kind.EMPTY:
            self.new_kind = random_neighbour.kind if random_neighbour.kind is not self.Kind.WALL else self.Kind.EMPTY
            self.changed = True
        elif self.kind == self.Kind.ROCK and random_neighbour.kind == self.Kind.PAPER:
            self.new_kind = self.Kind.PAPER
            self.changed = True
        elif self.kind == self.Kind.PAPER and random_neighbour.kind == self.Kind.SCISSORS:
            self.new_kind = self.Kind.SCISSORS
            self.changed = True
        elif self.kind == self.Kind.SCISSORS and random_neighbour.kind == self.Kind.ROCK:
            self.new_kind = self.Kind.ROCK
            self.changed = True

    def commit_color(self):
        if(self.changed):
            self.kind = self.new_kind
            self.color = self.KIND_COLORS[self.kind]
            self.changed = False
            return True
        return False
        
