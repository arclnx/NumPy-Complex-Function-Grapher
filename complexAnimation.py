import numpy as np
from PIL import Image
import color

class animation:
    """Create an animation that holds keyframes"""
    def __init__(self, colorfunc=None):
        self.keyframes = [] # list of all keyframes

    def addKeyframe(self, keyframe):
        self.keyframes.append(keyframe)
        pass

    def render(self, size=(1920,1080), folderPath=""):
        # create an array of the data fro each keyframe
        keyframeData = np.array([keyframe.calculate(size) for keyframe in self.keyframes])
        
        # create an array of the lengths of each keyframe
        keyframeLengths = np.array([keyframe.length for keyframe in self.keyframes])
        
        # set up frame data array as an empty 3d array with the correct width and height, and a depth of 0
        frameData = np.empty((0,size[0],size[1]))
        
        # loop through each keyframe, interpolate the interframes, and render them
        frameNumber = 0
        for keyFrameIndex in range(len(self.keyframes)-1):
            
            #set frameData to an array of 2d arrays of each frame
            frameData =  np.linspace(start=keyframeData[keyFrameIndex],
                                     stop=keyframeData[keyFrameIndex+1],
                                     num=keyframeLengths[keyFrameIndex]-1,
                                     endpoint=False)
            for frame in frameData:
                print(frame)
                print("--------------------------------------")
                # apply the complex->RGB function, then transpose to get the right shape
                renderedFrame = color.ComplexToRGB(frame)
                print(renderedFrame)
                print(renderedFrame.shape)
                print("--------------------------------------")
                print(renderedFrame.T)
                print(renderedFrame.T.ndim)
                # convert the np.ndarray to a PIL image
                frameImage = Image.fromarray(renderedFrame.T,"RGB")
                
                # set the filepath
                filePath = "C:\\Users\\trevo\\Desktop\\Grapher_Output\\" + str(frameNumber).rjust(4,"0") + ".png"
                # save the image
                frameImage.save(filePath)
                print("saved at: " + filePath)

        #frameData = np.concatenate((frameData, np.array([keyframeData[-1]])))
        #output = open(r"C:\Users\trevo\Desktop\output.txt", "w")
        #output.write(str(frameData))
        #output.close()
        #print(frameData.shape)

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
myanim.render((5,5))