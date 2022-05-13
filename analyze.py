import matplotlib.pyplot as plt
import numpy as np

# PLOT TouchSensorValues
# backLegTouchSensorValues = np.load("data/BackLegTouchSensors.npy");
# plt.plot(backLegTouchSensorValues, label="BackLegTouchSensors", linewidth=2);
# frontLegTouchSensorValues = np.load("data/FrontLegTouchSensors.npy");
# plt.plot(frontLegTouchSensorValues, label="FrontLegTouchSensors");
# plt.legend();

#PLOT motorValues

backLegMotorValues = np.load("data/Torso_BackLegCommands.npy");
frontLegMotorValues = np.load("data/Torso_FrontLegCommands.npy");
plt.plot(frontLegMotorValues);
plt.plot(backLegMotorValues);

plt.show();