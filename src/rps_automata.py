from rps_cell import RPS_Cell, RPS_Cell_Spiral
from automata import Automata
import pygame

class RPS_Automata(Automata):

    def __init__(self, width, height, windowsize, spiral = False, wrap = True, font = None):
        self.Cell = RPS_Cell
        if(spiral):
            self.Cell  = RPS_Cell_Spiral
        super().__init__(width,height,windowsize,wrap,font)
        self.selected_kind = self.Cell.Kind.EMPTY
        self.RPS_COLORS = {
            "red": (255,0,0),
            "green": (0,255,0),
            "blue": (0,0,255),
            "black": (0,0,0),
            "white": (255,255,255)
        }

    def setup_board(self):
        self.board = [ [self.Cell(x,y, self.Cell.Kind.EMPTY, cellsize=self.CELLSIZE, font = self.font) for y in range(self.height)] for x in range(self.width) ]
        for y in range(self.height):
            for x in range(self.width):
                self.logger.debug(f"assigning neighbors to {x},{y}")
                self.assign_neighbours_at(x,y)

    def handle_key_event(self, key, unicode):
        if key == pygame.K_1:
            self.logger.info("selected rock")
            self.selected_kind = self.Cell.Kind.ROCK
        elif key == pygame.K_2:
            self.logger.info("selected PAPER")
            self.selected_kind = self.Cell.Kind.PAPER
        elif key == pygame.K_3:
            self.logger.info("selected SCISSORS")
            self.selected_kind = self.Cell.Kind.SCISSORS
        elif key == pygame.K_4:
            self.logger.info("selected WALL")
            self.selected_kind = self.Cell.Kind.WALL
        elif key == pygame.K_5:
            self.logger.info("selected EMPTY")
            self.selected_kind = self.Cell.Kind.EMPTY
        else:
            self.logger.info(f"unhandled input: {unicode}")

    def mouse_click_at(self, pos):
        cell = self.board[pos[0]][pos[1]]
        cell.kind = self.selected_kind
        cell.color = cell.KIND_COLORS[cell.kind]


