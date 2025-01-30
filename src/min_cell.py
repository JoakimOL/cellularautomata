import random
from enum import Enum
from cell import Cell

class Min_Cell(Cell):
    def __init__(self, x, y, cellsize = 50, font = None):
        super().__init__(x,y, cellsize, font)

    def apply_rule(self):
        # hva er reglene i automaten din?

        # Her tar cellen samme farge som naboen til høyre
        # Ikke alle ruter har en nabo til høyre (hvis du er på kanten)
        # så husk å sjekke at den finnes, som vist under!
        if(not self.right_of):
            return
            # Husk å bare gi new_color ny verdi i denne funksjonen!
        if(self.right_of.color != self.color):
            self.new_color = self.right_of.color
            self.changed = True

    def commit_color(self):
        # Hvis cellen har endret seg, skriv
        # over variabelene som beskriver tilstanden
        # med verdiene som er nye
        #
        # I dette eksempelet skriver vi over "color" med "new_color"
        # fordi vi bare endrer farge
        if(self.changed):
            self.color = self.new_color
            self.changed = False
            return True
        return False
