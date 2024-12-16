import logging
import pygame

from cell import Cell

class Automata:
    def __init__(self, width, height, windowsize, colors, font = None):
        self.logger = logging.getLogger()
        smallest = min(windowsize[0], windowsize[1])
        self.CELLSIZE = int(smallest / width)
        self.width = width
        self.height = height
        self.colors = colors
        self.font = font
        self.setup_board()

    def __str__(self):
        return str(self.board)

    def assign_neighbours_at(self, x, y):
        cell = self.board[x][y]
        self.bounds_checked_add_neighbour_at(cell, x-1, y  )
        self.bounds_checked_add_neighbour_at(cell, x  , y-1)
        # self.bounds_checked_add_neighbour_at(cell, x-1, y-1)
        self.bounds_checked_add_neighbour_at(cell, x+1, y  )
        self.bounds_checked_add_neighbour_at(cell, x  , y+1)
        # self.bounds_checked_add_neighbour_at(cell, x+1, y+1)
        # self.bounds_checked_add_neighbour_at(cell, x+1, y-1)
        # self.bounds_checked_add_neighbour_at(cell, x-1, y+1)
        cell.initialized = True

    def setup_board(self):
        self.board = [ [Cell(x,y, cellsize=self.CELLSIZE, initial_color = (255,0,0), font = self.font) for y in range(self.height)] for x in range(self.width) ]
        # self.board = [ [Cell(x,y, cellsize=self.CELLSIZE, initial_color = list(self.colors.values())[(x+y)%3]) for y in range(self.height)] for x in range(self.width) ]
        for y in range(self.height):
            for x in range(self.width):
                self.logger.debug(f"assigning neighbors to {x},{y}")
                self.assign_neighbours_at(x,y)

    def bounds_checked_add_neighbour_at(self, cell, x, y):
        if(x >= self.width):
            x = self.width - x
        if(y >= self.height):
            y = self.height - y
        cell.neighbours.append(self.board[x][y])

    def draw(self, surface_to_draw_on):
        for line_of_cells in self.board:
            for cell in line_of_cells:
                cell.draw(surface_to_draw_on)

    def apply_rule(self):
        for line_of_cells in self.board:
            for cell in line_of_cells:
                cell.apply_rule()

    def commit_rule_result(self):
        updated = 0
        for line_of_cells in self.board:
            for cell in line_of_cells:
                if(cell.commit_color()):
                    updated += 1
        self.logger.info(f"{updated} cells updated")


    def mouse_click_at(self, pos, color):
        cell = self.board[pos[0]][pos[1]]
        cell.color = color

