from min_cell import Min_Cell
from automata import Automata
import pygame

class Min_Automata(Automata):

    def __init__(self, width, height, windowsize, wrap = True, font = None):
        super().__init__(width,height,windowsize,wrap,font)
        # Legg til det du trenger her!
        self.selected_color = (0,0,0)

    def setup_board(self):
        # Husk å legge til eventuelle parametre du legger til i din celle!
        self.board = [ [Min_Cell(x,y, cellsize=self.CELLSIZE, font = self.font) for y in range(self.height)] for x in range(self.width) ]
        for y in range(self.height):
            for x in range(self.width):
                self.logger.debug(f"assigning neighbors to {x},{y}")
                self.assign_neighbours_at(x,y)

    def handle_key_event(self, key, unicode):
        # Her kan du velge farger eller annen oppførsel når
        # man trykker på en knapp på tastaturet
        if key == pygame.K_1:
            self.logger.info("Valgte sort")
            self.selected_color = (0,0,0)
        elif key == pygame.K_2:
            self.logger.info("Valgte hvit")
            self.selected_color = (255,255,255)
        elif key == pygame.K_3:
            self.logger.info("Valgte rød")
            self.selected_color = (255,0,0)
        elif key == pygame.K_4:
            self.logger.info("Valgte blå")
            self.selected_color = (0,0,255)
        else:
            self.logger.info(f"unhandled input: {unicode}")

    def mouse_click_at(self, pos):
        # Her kan du bestemme hva som skjer når en celle blir trykket på
        # Kode som henter cellen som blir trykket på
        cell = self.board[pos[0]][pos[1]]

        # Hva vil du gjøre med cellen?
        # her setter vi fargen til den valgte fargen
        # i self.selected_color
        cell.color = self.selected_color


