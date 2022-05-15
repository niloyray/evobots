import pyrosim.pyrosim as pyrosim
import random
import numpy as np
import os

class SOLUTION:
    def __init__(self):
        self.weights = np.random.rand(3,2)
        self.weights = self.weights*2-1

    def Evaluate(self, directOrGUI):
        self.Create_World();
        self.Create_Body("body.urdf");
        self.Create_Brain("brain.nndf");
        os.system("python simulate.py" +" "+ directOrGUI)
        fitnessFile=open("fitness.txt")
        self.fitness=(float)(fitnessFile.read())
        # print(self.fitness)
    
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



