from enum import Enum
from cell import Cell

class GOL_Cell(Cell):
    def __init__(self, x, y, cellsize = 50, font = None):
        super().__init__(x,y, cellsize, font)
        self.living = False
        self.next_living = False
        self.live_color = (255,255,255)
        self.dead_color = (0,0,0)
        self.color = self.dead_color

    def apply_rule(self):

        number_of_life_neighbours = 0
        for neighbour in self.neighbours:
            if neighbour.living:
                number_of_life_neighbours += 1

        if self.living:
            if number_of_life_neighbours < 2:
                self.next_living = False
                self.changed = True
            elif number_of_life_neighbours > 3:
                self.next_living = False
                self.changed = True
        elif not self.living:
            if number_of_life_neighbours == 3:
                self.next_living = True
                self.changed = True

    def commit_color(self):
        if(self.changed):
            self.logger.info(f"going from {self.living} to {self.next_living}")
            self.living = self.next_living
            if self.next_living:
                self.color = self.live_color
            else:
                self.color = self.dead_color
            self.changed = False
            return True
        return False
        
