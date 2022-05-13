import matplotlib.pyplot as plt
import numpy as np

# PLOT TouchSensorValues
# backLegTouchSensorValues = np.load("data/backLegTouchSensorValues.npy");
# plt.plot(backLegTouchSensorValues, label="backLegTouchSensorValues", linewidth=2);
# frontLegTouchSensorValues = np.load("data/frontLegTouchSensorValues.npy");
# plt.plot(frontLegTouchSensorValues, label="frontLegTouchSensorValues");
# plt.legend();

#PLOT targetAngles
targetAngles = np.load("data/targetAngles.npy");
plt.plot(targetAngles);

plt.show();