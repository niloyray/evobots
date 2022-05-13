from world import WORLD
from robot import ROBOT
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time
from datetime import datetime
import constants as c

from robot import ROBOT

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath());

        self.world = WORLD();
        self.robot = ROBOT();

        print(pybullet_data.getDataPath());
        p.setGravity(0, 0, -9.8);

    def __del__(self):
        p.disconnect();

    def Run(self):
        startTime = datetime.now() 
        for t in range(c.iterations):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Act(t)
            
            time.sleep(c.waitInterval);
        print("  >>> Time Taken: ",datetime.now() - startTime)
        self.robot.Save_Sensor_Values();
        self.robot.Save_Motor_Values(); 