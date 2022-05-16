import pyrosim.pyrosim as pyrosim
import random
import numpy as np
import os
import time

class SOLUTION:
    def __init__(self,nextAvailableID):
        self.weights = np.random.rand(3,2)
        self.weights = self.weights*2-1
        self.myID = nextAvailableID

    def Start_Simulation(self, directOrGUI):
        self.Create_World();
        self.Create_Body("body.urdf");
        self.Create_Brain("brain"+str(self.myID)+".nndf");
        os.system("start /B python simulate.py" +" "+ directOrGUI + " " +str(self.myID))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(0.01)
        fitnessFile=open("fitness"+str(self.myID)+".txt")
        self.fitness=(float)(fitnessFile.read())
        print("\n>>> Fitness for "+str(self.myID)+":"+str(self.fitness)+"\n")
        fitnessFile.close()
        time.sleep(0.1)
        os.system("del fitness"+str(self.myID)+".txt")

    def Mutate(self):
        rowToMutate=random.randint(0,2)
        columnToMutate=random.randint(0,1)
        self.weights[rowToMutate,columnToMutate]=random.random()*2-1

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf");
        
        x=-2;
        y=2;
        z=0.5;
        length = 1;
        width = 1;
        height = 1;
        
        pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height]);
        pyrosim.End();



    def Create_Body(self,bodyUrdf):
        robotId = pyrosim.Start_URDF(bodyUrdf);
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[1,1,1]);
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[1,1,1]);
        pyrosim.Send_Joint(name = "Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1.0,0,1.0]);
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[1,1,1]);
        pyrosim.Send_Joint(name = "Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2.0,0,1.0]);
        pyrosim.End();

    def Create_Brain(self,brainNndf):
        pyrosim.Start_NeuralNetwork(brainNndf);
        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso");
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg");
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg");
        pyrosim.Send_Motor_Neuron(name = 3, jointName = "Torso_BackLeg");
        pyrosim.Send_Motor_Neuron(name = 4, jointName = "Torso_FrontLeg");
        for currentRow in range(0,3):
            for currentColumn in range(0,2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])
        pyrosim.End();

    def Set_ID(self, nextAvailableID):
        self.myID=nextAvailableID

