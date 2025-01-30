from powder_cell import Powder_Cell
from automata import Automata
import pygame

class Powder_Automata(Automata):

    def __init__(self, width, height, windowsize, spiral = False, wrap = True, font = None):
        super().__init__(width,height,windowsize,wrap,font)
        self.selected_kind = Powder_Cell.Kind.EMPTY
        self.COLORS = {
            Powder_Cell.Kind.EMPTY: (0,0,0),
            Powder_Cell.Kind.SAND: (216,179,130),
        }

    def setup_board(self):
        self.board = [ [Powder_Cell(x,y, cellsize=self.CELLSIZE, font = self.font) for y in range(self.height)] for x in range(self.width) ]
        for y in range(self.height):
            for x in range(self.width):
                self.logger.debug(f"assigning neighbors to {x},{y}")
                self.assign_neighbours_at(x,y)

    def handle_key_event(self, key, unicode):
        if key == pygame.K_1:
            self.logger.info("selected sand")
            self.selected_kind = Powder_Cell.Kind.SAND
        elif key == pygame.K_2:
            self.logger.info("selected water")
            self.selected_kind = Powder_Cell.Kind.WATER
        elif key == pygame.K_5:
            self.logger.info("selected EMPTY")
            self.selected_kind = Powder_Cell.Kind.EMPTY
        else:
            self.logger.info(f"unhandled input: {unicode}")

    def mouse_click_at(self, pos):
        cell = self.board[pos[0]][pos[1]]
        cell.kind = self.selected_kind
        cell.color = cell.KIND_COLORS[cell.kind]


