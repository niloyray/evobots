from sensor import SENSOR
from motor import MOTOR
import numpy as np
import constants as c
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:
    def __init__(self, solutionID) -> None:
        self.robotId = p.loadURDF("body.urdf");
        self.nn = NEURAL_NETWORK("brain"+str(solutionID)+".nndf")
        pyrosim.Prepare_To_Simulate(self.robotId);
        self.Prepare_To_Sense();
        self.Prepare_To_Act();
        os.system("del brain"+str(solutionID)+".nndf")

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
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robotId,desiredAngle);
    
    def Save_Motor_Values(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName].Save_Values();

    def Think(self,t):
        self.nn.Update();
        # self.nn.Print();
    
    def Get_Fitness(self,solutionID):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero=positionOfLinkZero[0]
        tmpFitnessFile=open("tmp"+str(solutionID)+".txt", "w")
        tmpFitnessFile.write(str(xCoordinateOfLinkZero))
        tmpFitnessFile.close()
        os.rename("tmp"+str(solutionID)+".txt" , "fitness"+str(solutionID)+".txt")

        # print(xCoordinateOfLinkZero)
        # exit()