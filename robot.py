from sensor import SENSOR
from motor import MOTOR
import numpy as np
import constants as c
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim


class ROBOT:
    def __init__(self) -> None:
        # self.backLegTouchSensor = SENSOR()
        # self.frontLegTouchSensor = SENSOR()
        # self.backLegMotor = MOTOR()
        # self.frontLegMotor = MOTOR()
        # amplitudeBackLeg = c.amplitudeBackLeg;
        # frequencyBackLeg = c.frequencyBackLeg;
        # phaseOffsetBackLeg = c.phaseOffsetBackLeg;

        # amplitudeFrontLeg = c.amplitudeFrontLeg;
        # frequencyFrontLeg = c.frequencyFrontLeg;
        # phaseOffsetFrontLeg = c.phaseOffsetFrontLeg;
        self.robotId = p.loadURDF("body.urdf");
        pyrosim.Prepare_To_Simulate(self.robotId);
        self.Prepare_To_Sense();
        self.Prepare_To_Act();

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName);
    
    def Sense(self,t):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Get_Value(t);
    
    def Save_Sensor_Values(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Save_Values();

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName);


    def Act(self,t):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName].Set_Value(self.robotId,t);
    
    def Save_Motor_Values(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName].Save_Values();