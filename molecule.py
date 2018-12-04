import numpy as np

class Molecule():

    def __init__(self, type="H", pos=np.array([1,1,1]), vel=np.array([1,1,1])):
        self.type = type
        self.pos = pos
        self.vel = vel

    def set_position(self, pos):
        self.pos = pos

    def get_position(self):
        return self.pos

    def set_velocity(self, vel):
        self.vel = vel

    def get_velocity(self):
        return self.vel