from block import Block
from postion import Postion

class LBlock(Block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [Postion(0,2), Postion(1,0), Postion(1,1), Postion(1,2)],
            1: [Postion(0,1), Postion(1,1), Postion(2,1), Postion(2,2)],
            2: [Postion(1,0), Postion(1,1), Postion(1,2), Postion(2,0)],
            3: [Postion(0,0), Postion(0,1), Postion(1,1), Postion(2,1)]
        }


class JBlock(Block):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0: [Postion(0,0), Postion(1,0), Postion(1,1), Postion(1,2)],
            1: [Postion(0,1), Postion(0,2), Postion(1,1), Postion(2,1)],
            2: [Postion(1,0), Postion(1,1), Postion(1,2), Postion(2,2)],
            3: [Postion(0,1), Postion(1,1), Postion(2,0), Postion(2,1)]
        }


class IBlock(Block):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [Postion(1,0), Postion(1,1), Postion(1,2), Postion(1,3)],
            1: [Postion(0,2), Postion(1,2), Postion(2,2), Postion(3,2)],
            2: [Postion(2,0), Postion(2,1), Postion(2,2), Postion(2,3)],
            3: [Postion(0,1), Postion(1,1), Postion(2,1), Postion(3,1)]
        }

class OBlock(Block):
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0: [Postion(0,0), Postion(0,1), Postion(1,0), Postion(1,1)]
            
        }

class SBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0: [Postion(0,1), Postion(0,2), Postion(1,0), Postion(1,1)],
            1: [Postion(0,1), Postion(1,1), Postion(1,2), Postion(2,2)],
            2: [Postion(1,1), Postion(1,2), Postion(2,0), Postion(2,1)],
            3: [Postion(0,0), Postion(1,0), Postion(1,1), Postion(2,1)]
        }

class TBlock(Block):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0: [Postion(0,1), Postion(1,0), Postion(1,1), Postion(1,2)],
            1: [Postion(0,1), Postion(1,1), Postion(1,2), Postion(2,1)],
            2: [Postion(1,0), Postion(1,1), Postion(1,2), Postion(2,1)],
            3: [Postion(0,1), Postion(1,0), Postion(1,1), Postion(2,1)]
        }


class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0: [Postion(0,0), Postion(0,1), Postion(1,1), Postion(1,2)],
            1: [Postion(0,2), Postion(1,1), Postion(1,2), Postion(2,1)],
            2: [Postion(1,0), Postion(1,1), Postion(2,1), Postion(2,2)],
            3: [Postion(0,1), Postion(1,0), Postion(1,1), Postion(2,0)]
        }