import numpy as np
from kinematics_calc import euler

@euler("ZYZ")
def eulerZYZ(t):
    angle = np.array([0., 0., 0.])
    c = np.sqrt(1-t[2][2]**2)
    angle[0] = np.arctan2(t[1][2], t[0][2])
    angle[1] = np.arctan2(c,t[2][2])
    angle[2] = np.arctan2(t[2][1], -t[2][0])
    return angle