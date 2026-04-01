import numpy as np

class SpaceObject:
    def __init__(self, id, r, v, type):
        self.id = id
        self.r = np.array(r, dtype=float)
        self.v = np.array(v, dtype=float)
        self.type = type