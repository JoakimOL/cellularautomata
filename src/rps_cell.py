import random
from enum import Enum
from cell import Cell

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
        
class RPS_Cell_Spiral(Cell):
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
        limit = 2
        rock,scissors,paper = 0,0,0
        for neighbour in self.neighbours:
            if neighbour.kind == self.Kind.PAPER:
                paper += 1
            elif neighbour.kind == self.Kind.ROCK: 
                rock += 1
            elif neighbour.kind == self.Kind.SCISSORS: 
                scissors += 1
        if self.kind in [self.Kind.ROCK, self.Kind.EMPTY] and paper > limit:
            self.new_kind = self.Kind.PAPER
            self.changed = True
        elif self.kind in [self.Kind.PAPER, self.Kind.EMPTY] and scissors > limit:
            self.new_kind = self.Kind.SCISSORS
            self.changed = True
        elif self.kind in [self.Kind.SCISSORS, self.Kind.EMPTY] and rock > limit:
            self.new_kind = self.Kind.ROCK
            self.changed = True

    def commit_color(self):
        if(self.changed):
            self.kind = self.new_kind
            self.color = self.KIND_COLORS[self.kind]
            self.changed = False
            return True
        return False
        
