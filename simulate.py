import pybullet as p
import time
from datetime import datetime

physicsClient = p.connect(p.GUI)

startTime = datetime.now() 
for i in range(500):
  p.stepSimulation()
  time.sleep(0.01)
print("  >>> Time Taken: ",datetime.now() - startTime) 

p.disconnect()
