<<<<<<< HEAD
import pyrosim.pyrosim as pyrosim


x = 0;

pyrosim.Start_SDF("boxes.sdf");

for i in range(10):
  x+=1
  y = 0
  for j in range(10):
    y += 1
    a = 1
    z = 0.5
    length = 1
    width = 1
    height = 1
    for k in range(10):
      pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height]);
      length = length*0.9;
      width = width*0.9;
      height = height*0.9;
      a += height;
      z=a-height/2;

=======
import pyrosim.pyrosim as pyrosim


x = 0;

pyrosim.Start_SDF("boxes.sdf");

for i in range(10):
  x+=1
  y = 0
  for j in range(10):
    y += 1
    a = 1
    z = 0.5
    length = 1
    width = 1
    height = 1
    for k in range(10):
      pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height]);
      length = length*0.9;
      width = width*0.9;
      height = height*0.9;
      a += height;
      z=a-height/2;

>>>>>>> 6cdffc2413c99acc081276efacc297172f921cd9
pyrosim.End();