import input_class as ic
import manipulator_data as md
import kinematics_calc as kc
import os

for f in os.listdir('plugins'):
    if f.endswith('.py'):
        __import__('plugins.'+f[:-3])

IO = ic.InputOutputData()

iiwa = md.ManipulatorData()

kinematic = kc.Kinematics()

iiwa.setD(IO.input_data())
iiwa.setThetta(IO.input_data())
iiwa.setAlpha(IO.input_data())
iiwa.setA(IO.input_data())

kinematic.FK(iiwa.getD(), iiwa.getThetta(), iiwa.getAlpha(), iiwa.getA())

IO.output_data(kinematic.getJoint())

print(kinematic.calcAngles('ZYZ'))
