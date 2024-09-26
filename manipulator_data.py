import numpy as np

class ManipulatorData:
    def __init__(self):
        self.d_ = np.array([])
        self.thetta_ = np.array([])
        self.alpha_ = np.array([])
        self.a_ = np.array([])
    
    # ---------------------------- all
    
    def setParams(self, d, thetta, alpha, a):
        self.d_ = d.copy()
        self.thetta_ = np.deg2rad(thetta).copy()
        self.alpha_ = np.deg2rad(alpha).copy()
        self.a_ = a.copy()

    def getParams(self):
        return self.d_, self.thetta_, self.alpha_, self.a_ 
    
    # ---------------------------- d
    def setD(self, d):
        self.d_ = d.copy()

    def getD(self):
        return self.d_
    
    # ---------------------------- thetta
    def setThetta(self, thetta):
        self.thetta_ = np.deg2rad(thetta).copy()

    def getThetta(self):
        return self.thetta_
    
    # ---------------------------- alpha
    def setAlpha(self, alpha):
        self.alpha_ = np.deg2rad(alpha).copy()

    def getAlpha(self):
        return self.alpha_
    
    # ---------------------------- a
    def setA(self, a):
        self.a_ = a.copy()

    def getA(self):
        return self.a_
