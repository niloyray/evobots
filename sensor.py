import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self,linkName):
        self.linkName = linkName;
        self.Prepare_To_Sense();
    
    def Prepare_To_Sense(self):
        self.values = np.zeros(c.iterations);

    def Get_Value(self,t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName);
        if t == c.iterations - 1: 
            print(self.values);
    
    def Save_Values(self):
        np.save("data/"+self.linkName+"TouchSensors.npy", self.values);
