
from gol_cell import GOL_Cell
from automata import Automata
import pygame

class GOL_Automata(Automata):

    def __init__(self, width, height, windowsize, wrap = True, font = None):
        super().__init__(width,height,windowsize,wrap,font)
        self.selected = False

    def setup_board(self):
        self.board = [ [GOL_Cell(x,y, cellsize=self.CELLSIZE, font = self.font) for y in range(self.height)] for x in range(self.width) ]
        for y in range(self.height):
            for x in range(self.width):
                self.logger.debug(f"assigning neighbors to {x},{y}")
                self.assign_neighbours_at(x,y)

    def handle_key_event(self, key, unicode):
        if key == pygame.K_1:
            self.logger.info("selected death")
            self.selected = False
        elif key == pygame.K_2:
            self.logger.info("selected life")
            self.selected = True
        else:
            self.logger.info(f"unhandled input: {unicode}")

    def mouse_click_at(self, pos):
        cell = self.board[pos[0]][pos[1]]
        # cell.set_living(self.selected)
        cell.living = self.selected
        cell.color = cell.live_color if cell.living else cell.dead_color


