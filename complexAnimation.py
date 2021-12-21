import numpy as np
from numpy.core.function_base import linspace

class animation:
    """Create an animation that holds keyframes"""
    def __init__(self, colorfunc=None):
        self.keyframes = [] # list of all keyframes

    def addKeyframe(self, keyframe):
        self.keyframes.append(keyframe)
        pass

    def render(self, size=(1920,1080)):
        # create an array of the data fro each keyframe
        keyframeData = np.array([keyframe.calculate(size) for keyframe in self.keyframes])
        # create an array of the lengths of each keyframe
        keyframeLengths = np.array([keyframe.length for keyframe in self.keyframes])
        # set up frame data array as an empty 3d array with the correct width and height, and a depth of 0
        frameData = np.empty((0,size[0],size[1]))
        # loop through each keyframe, interpolate the interframes, and append them to frameData
        for frameIndex in range(len(self.keyframes)-1):

            frameData = np.concatenate((frameData,
                                        np.linspace(start=keyframeData[frameIndex],
                                                    stop=keyframeData[frameIndex+1],
                                                    num=keyframeLengths[frameIndex]-1,
                                                    endpoint=False)))
        frameData = np.concatenate((frameData, np.array([keyframeData[-1]])))
        output = open(r"C:\Users\trevo\Desktop\output.txt", "w")
        output.write(str(frameData))
        output.close()

class keyframe:
    """create a keyframe that holds data about the function, length, etc."""
    def __init__(self, min=(-1,-1), max=(1,1), function="x", length=60): 
        self.xmin, self.ymin = min # min and max should be a pair of reals, not an imaginry 
        self.xmax, self.ymax = max
        self.function = lambda x:eval(function)
        self.funcstring = function
        self.length = length # the number of frames between this keyframe and the next
                             # [start,stop), except for last keyframe, which only renders its first frame

    
    def calculate(self, size=(1920,1080)):
        """calculate the values of the function"""

        print("╔══════════════════════════════")
        print("║  calculating keyframe...  ")
        print("║  xmin: " + str(self.xmin) + "; ymin: " + str(self.ymin))
        print("║  xmax: " + str(self.xmax) + "; ymax: " + str(self.ymax))
        print("║  function: f(x)=" + self.funcstring)

        # generate a 2d matrix of complex numbers
        real = np.linspace(self.xmin, self.xmax, size[0])
        complex = np.linspace(self.ymin, self.ymax, size[1])
        real, complex = np.meshgrid(real, complex, indexing='ij')
        cplane = real + complex*1j

        # map function over the plane
        cplane = self.function(cplane)
        print("║  Done!")
        print("╚══════════════════════════════")
        
        return(cplane)
        
        
        
myanim = animation()
a = keyframe(length=4)
b = keyframe(length=4)
myanim.addKeyframe(a)
myanim.addKeyframe(b)
print(a.length)
myanim.render((2,4))