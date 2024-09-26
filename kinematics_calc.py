import numpy as np

class Kinematics:
    angles = {}
    def __init__(self):
        print("kinematics on")

    def T(self, d, thetta, alpha, a):
        return np.array([[np.cos(thetta), -np.sin(thetta)*np.cos(alpha), np.sin(thetta)*np.sin(alpha), a*np.cos(thetta)],
                  [np.sin(thetta), np.cos(thetta)*np.cos(alpha), -np.cos(thetta)*np.sin(alpha), a*np.sin(thetta)], 
                  [0, np.sin(alpha), np.cos(alpha), d], 
                  [0, 0, 0, 1]])
    
    def FK(self, d, thetta, alpha, a):
        self.temp_t = np.eye(4)
        N = len(d)

        self.joint = np.array([[0, 0, 0]])

        for i in range(0,N):
            self.temp_t = self.temp_t @ self.T(d[i], thetta[i], alpha[i], a[i])
            coordinate = np.array([self.temp_t[0][3], self.temp_t[1][3], self.temp_t[2][3]])
            self.joint = np.vstack([self.joint, coordinate])

        self.endefector_pos = [[self.joint[N]], [self.joint[N]], [self.joint[N]]]

        return self.temp_t, self.joint, self.endefector_pos
    
    def getT(self):
        return self.temp_t
    
    def getJoint(self):
        return self.joint
    
    def getEndpose(self):
        return self.endefector_pos
    
    def calcAngles(self, comb):
        return self.angles[comb](self.temp_t)

def euler(comb): # Декоратор
    def decorator(fun):
        def wrapper(t):
            return fun(t)
        Kinematics.angles[comb] = wrapper
        return wrapper
    return decorator