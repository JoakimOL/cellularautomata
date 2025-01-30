import logging
import pygame

from cell import Simple_Cell

class Automata:
    def __init__(self, width, height, windowsize, wrap = True, font = None):
        self.logger = logging.getLogger()
        self.RED = (255,0,0)
        self.GREEN = (0,255,0)
        self.BLUE = (0,0,255)
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)

        self.colors = {
            "red": self.RED,
            "green": self.GREEN,
            "blue": self.BLUE,
            "black": self.BLACK,
            "white": self.WHITE
        }
        smallest = min(windowsize[0], windowsize[1])
        self.CELLSIZE = int(smallest / width)
        self.width = width
        self.height = height
        self.selected_color = self.colors["black"]
        self.font = font
        self.wrap = wrap
        self.setup_board()

    def __str__(self):
        return str(self.board)

    def assign_neighbours_at(self, x, y):
        cell = self.board[x][y]
        cell.left_of      = self.bounds_checked_add_neighbour_at(cell, x-1, y  , self.wrap)
        cell.above        = self.bounds_checked_add_neighbour_at(cell, x  , y-1, self.wrap)
        cell.above_left   = self.bounds_checked_add_neighbour_at(cell, x-1, y-1, self.wrap)
        cell.right_of     = self.bounds_checked_add_neighbour_at(cell, x+1, y  , self.wrap)
        cell.below        = self.bounds_checked_add_neighbour_at(cell, x  , y+1, self.wrap)
        cell.below_right = self.bounds_checked_add_neighbour_at(cell, x+1, y+1, self.wrap)
        cell.above_right  = self.bounds_checked_add_neighbour_at(cell, x+1, y-1, self.wrap)
        cell.below_left  = self.bounds_checked_add_neighbour_at(cell, x-1, y+1, self.wrap)
        cell.initialized = True

    def setup_board(self):
        self.logger.warn("trying to initialize the base automaton")

    def bounds_checked_add_neighbour_at(self, cell, x, y, wrap = True):
        if(x >= self.width and wrap):
            x = self.width - x
        elif (x >= self.width or x < 0 and not wrap):
            return
        if(y >= self.height and wrap):
            y = self.height - y
        elif (y >= self.width or y < 0 and not wrap):
            return
        neighbour = self.board[x][y]
        cell.neighbours.append(neighbour)
        return neighbour

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


    def mouse_click_at(self, pos):
        self.logger.warn("mouse_click_at in base automaton!")

    def handle_key_event(self, key, unicode):
        self.logger.warn("handle_key_event in base automaton!")
        

class Simple_Automata(Automata):
    def __init__(self, width, height, windowsize, wrap = True, font = None):
        super().__init__(width,height,windowsize,wrap,font)

    def setup_board(self):
        self.board = [ [Simple_Cell(x,y, cellsize=self.CELLSIZE, initial_color = self.colors["white"], font = self.font) for y in range(self.height)] for x in range(self.width) ]
        for y in range(self.height):
            for x in range(self.width):
                self.logger.debug(f"assigning neighbors to {x},{y}")
                self.assign_neighbours_at(x,y)

    def mouse_click_at(self, pos):
        cell = self.board[pos[0]][pos[1]]
        cell.color = self.selected_color

    def handle_key_event(self, key, unicode):
        if key == pygame.K_1:
            self.logger.info("selected red")
            self.selected_color = self.colors["red"]
        elif key == pygame.K_2:
            self.logger.info("selected green")
            self.selected_color = self.colors["green"]
        elif key == pygame.K_3:
            self.logger.info("selected blue")
            self.selected_color = self.colors["blue"]
        elif key == pygame.K_4:
            self.logger.info("selected black")
            self.selected_color = self.colors["black"]
        elif key == pygame.K_5:
            self.logger.info("selected white")
            self.selected_color = self.colors["white"]
        else:
            self.logger.info(f"unhandled input: {unicode}")
