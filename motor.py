import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self,jointName):
        self.jointName = jointName;
        self.Prepare_To_Act();
    
    def Prepare_To_Act(self):
        self.motorValues = np.zeros(c.iterations);
        self.amplitude = c.amplitude;
        self.frequency = c.frequency;
        self.phaseOffset = c.phaseOffset;
        targetAngles = np.linspace(0,2*np.pi,c.iterations);
        if self.jointName == "Torso_BackLeg":
            self.frequency=5*c.frequency;
        for t in range(c.iterations):
            self.motorValues[t] =self.amplitude*np.sin(self.frequency*targetAngles[t]+self.phaseOffset);

    def Set_Value(self,robotId, t):
        pyrosim.Set_Motor_For_Joint( bodyIndex = robotId, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = self.motorValues[t], maxForce = 20);

    def Save_Values(self):
        np.save("data/"+self.jointName+"Commands.npy", self.motorValues);