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
    def __init__(self,directOrGUI,solutionID):
        self.directOrGUI = directOrGUI
        self.solutionID = solutionID
        if(directOrGUI=="DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath());
        self.world = WORLD();
        self.robot = ROBOT(solutionID);
        p.setGravity(0, 0, -9.8);

    def __del__(self):
        p.disconnect();

    def Run(self):
        startTime = datetime.now() 
        for t in range(c.iterations):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think(t)
            self.robot.Act(t)
            if(self.directOrGUI=="GUI"):
                time.sleep(c.waitInterval);
        print("\n")
        print(">>> Time Taken for",self.solutionID,":",datetime.now() - startTime)
        print("\n")
        self.robot.Save_Sensor_Values();

    def Get_Fitness(self,solutionID):
        self.robot.Get_Fitness(solutionID)