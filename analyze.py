import matplotlib.pyplot as plt
import numpy as np

backLegTouchSensorValues = np.load("data/backLegTouchSensorValues.npy");
plt.plot(backLegTouchSensorValues, label="backLegTouchSensorValues", linewidth=2);
frontLegTouchSensorValues = np.load("data/frontLegTouchSensorValues.npy");
plt.plot(frontLegTouchSensorValues, label="frontLegTouchSensorValues");
plt.legend();
plt.show();