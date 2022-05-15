import os
from hillclimber import HILL_CLIMBER

# for i in range(10):
#     os.system("python generate.py")
#     os.system("python simulate.py")

hc = HILL_CLIMBER()
hc.Evolve()
hc.Show_Best()