import numpy as np
import matplotlib.pyplot as plt

class InputOutputData:
    def __init__(self):
        self.xlim = [-1000, 1000]
        self.ylim = [-1000, 1000]
        self.zlim = [0, 1300]
        print("Hello")
        self.N = int(input("Input N of joints: "))
    
    def input_data(self):
        print("Input data:")
        data = list(map(lambda a: int(a) if a.lstrip("-").isdigit() else 0, input().split(" "))) # лямбда
        # print(data)
        if len(data) != self.N:
            raise ValueError('Lengths does not match')
        return np.array(data)
        
    def output_data(self, joint):
        fig = plt.figure()

        ax = plt.axes(projection="3d")
        plt.axis('equal')

        ax.set_xlim3d(self.xlim)
        ax.set_ylim3d(self.ylim)
        ax.set_zlim3d(self.zlim)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")

        print(joint)

        ax.plot3D(joint.T[0], joint.T[1], joint.T[2], 'red')
        ax.scatter3D(joint.T[0], joint.T[1], joint.T[2])

        plt.show()