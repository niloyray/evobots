import pybullet_data
import pybullet as p
import time
from datetime import datetime
import pyrosim.pyrosim as pyrosim
import numpy as np


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
for i in range(2000):
  p.stepSimulation()
  
  backLegTouchSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg");
  frontLegTouchSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg");
  pyrosim.Set_Motor_For_Joint( bodyIndex = robotId, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = 0.0, maxForce = 500);
  
  time.sleep(0.01)
print("  >>> Time Taken: ",datetime.now() - startTime) 

print("backLegTouchSensorValues: ", backLegTouchSensorValues);
np.save("data/backLegTouchSensorValues.npy", backLegTouchSensorValues);
print("frontLegTouchSensorValues: ", frontLegTouchSensorValues);
np.save("data/frontLegTouchSensorValues.npy", frontLegTouchSensorValues);
p.disconnect()
