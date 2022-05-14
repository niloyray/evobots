import pyrosim.pyrosim as pyrosim
import random

def Create_World():
  pyrosim.Start_SDF("world.sdf");
  
  x=-2;
  y=2;
  z=0.5;
  length = 1;
  width = 1;
  height = 1;
  
  pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height]);
  
  pyrosim.End();



def Create_Robot():
  Generate_Body("body.urdf");
  Generate_Brain("brain.nndf");


def Generate_Body(bodyUrdf):
  robotId = pyrosim.Start_URDF(bodyUrdf);
  pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[1,1,1]);
  pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[1,1,1]);
  pyrosim.Send_Joint(name = "Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1.0,0,1.0]);
  pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[1,1,1]);
  pyrosim.Send_Joint(name = "Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2.0,0,1.0]);
  pyrosim.End();

def Generate_Brain(brainNndf):
  pyrosim.Start_NeuralNetwork(brainNndf);
  pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso");
  pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg");
  pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg");
  pyrosim.Send_Motor_Neuron(name = 3, jointName = "Torso_BackLeg");
  pyrosim.Send_Motor_Neuron(name = 4, jointName = "Torso_FrontLeg");
  for s in range(0,3):
    for m in range(3,5):
      pyrosim.Send_Synapse(sourceNeuronName=s,targetNeuronName=m, weight=(random.random()-0.5)*2)

  pyrosim.End();


Create_World();
Create_Robot();
