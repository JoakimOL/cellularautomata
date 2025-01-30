from enum import Enum
from cell import Cell
class Powder_Cell(Cell):
    class Kind(Enum):
        EMPTY = 0
        SAND = 1
        WATER = 2

    KIND_COLORS = {
        Kind.EMPTY: (0,0,0),
        Kind.SAND: (216,179,130),
        Kind.WATER: (0,50,230),
    }
    
    def __init__(self, x, y, kind = Kind.EMPTY, cellsize = 50, font = None):
        super().__init__(x,y, cellsize, font)
        self.kind = kind
        self.color = self.KIND_COLORS[self.kind]

    def apply_rule(self):
        if self.changed:
            return
        if(self.kind == self.Kind.SAND):
            self.sink()
        if(self.kind == self.Kind.WATER):
            self.fall()
            if(self.changed):
                return
            self.disperse()

    def disperse(self):
        if not (self.below):
            return
        if self.below_right and self.below_right.kind == self.Kind.EMPTY:
            self.below_right.new_kind = self.kind
            self.new_kind = self.below_right.kind
            self.changed = True
            self.below_right.changed = True
        elif self.below_left and self.below_left.kind == self.Kind.EMPTY:
            self.below_left.new_kind = self.kind
            self.new_kind = self.below_left.kind
            self.changed = True
            self.below_left.changed = True
        return

    def fall(self):
        if self.below and self.below.kind  == self.Kind.EMPTY:
            self.below.new_kind = self.kind
            self.new_kind = self.below.kind
            self.changed = True
            self.below.changed = True

    def sink(self):
        if self.below and self.below.kind != self.Kind.SAND:
            self.below.new_kind = self.kind
            self.new_kind = self.below.kind
            self.changed = True
            self.below.changed = True
    

    def commit_color(self):
        if(self.changed):
            self.kind = self.new_kind
            self.color = self.KIND_COLORS[self.kind]
            self.changed = False
            return True
        return False
        
