import pybullet as p

class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane100.urdf");
        p.loadSDF("world.sdf");