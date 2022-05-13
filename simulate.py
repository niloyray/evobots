from random import random
import pybullet_data
import pybullet as p
import time
from datetime import datetime
import pyrosim.pyrosim as pyrosim
import numpy as np

amplitudeBackLeg = np.pi/4.0;
frequencyBackLeg = 10;
phaseOffsetBackLeg = 0;

amplitudeFrontLeg = np.pi/4.0;
frequencyFrontLeg = 10;
phaseOffsetFrontLeg = -np.pi/2;

iterations = 1000;
waitInterval = 1.0/240;

# targetAngles = np.sin(np.linspace(0,2*np.pi,iterations));
# targetAngles=targetAngles*np.pi/4.0;

targetAnglesBackLeg = np.linspace(0,2*np.pi,iterations);
targetAnglesFrontLeg = np.linspace(0,2*np.pi,iterations);
for i in range(iterations):
  targetAnglesBackLeg[i] = amplitudeBackLeg*np.sin(frequencyBackLeg*targetAnglesBackLeg[i]+phaseOffsetBackLeg);
  targetAnglesFrontLeg[i] = amplitudeFrontLeg*np.sin(frequencyFrontLeg*targetAnglesFrontLeg[i]+phaseOffsetFrontLeg);

np.save("data/targetAngles.npy",np.column_stack((targetAnglesBackLeg,targetAnglesFrontLeg)));
# exit();

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath());

print(pybullet_data.getDataPath());
backLegTouchSensorValues = np.zeros(2000);
frontLegTouchSensorValues = np.zeros(2000);

p.setGravity(0, 0, -9.8);
planeId = p.loadURDF("plane100.urdf");

robotId = p.loadURDF("body.urdf");
p.loadSDF("world.sdf");
pyrosim.Prepare_To_Simulate(robotId);

startTime = datetime.now() 
for i in range(iterations):
  p.stepSimulation()
  targetBL = random()*np.pi/2-np.pi/4.0;
  targetFL = random()*np.pi/2-np.pi/4.0; 
  backLegTouchSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg");
  frontLegTouchSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg");
  pyrosim.Set_Motor_For_Joint( bodyIndex = robotId, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesBackLeg[i], maxForce = 20);
  pyrosim.Set_Motor_For_Joint( bodyIndex = robotId, jointName = "Torso_FrontLeg", controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesFrontLeg[i], maxForce = 20);
  
  time.sleep(waitInterval);
print("  >>> Time Taken: ",datetime.now() - startTime) 

print("backLegTouchSensorValues: ", backLegTouchSensorValues);
np.save("data/backLegTouchSensorValues.npy", backLegTouchSensorValues);
print("frontLegTouchSensorValues: ", frontLegTouchSensorValues);
np.save("data/frontLegTouchSensorValues.npy", frontLegTouchSensorValues);
p.disconnect()
