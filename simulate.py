import pybullet_data
import pybullet as p
import time
from datetime import datetime

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath());

print(pybullet_data.getDataPath());

p.setGravity(0, 0, -9.8);
planeId = p.loadURDF("plane100.urdf");

robotId = p.loadURDF("body.urdf");
p.loadSDF("world.sdf");

startTime = datetime.now() 
for i in range(2000):
  p.stepSimulation()
  time.sleep(0.01)
print("  >>> Time Taken: ",datetime.now() - startTime) 


p.disconnect()
