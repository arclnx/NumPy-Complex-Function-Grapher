import numpy as np

class animation:
    """Create an animation that holds keyframes"""
    def __init__(self, width=1920, height=1080, colorfunc=None):
        self.width, self.height = width, height #resolution of animation in pixels
        self.keyframes = [] #list of all keyframes

    def addKeyframe(self, keyframe):
        self.keyframes.append(keyframe)
        pass


class keyframe:
    """create a keyframe that holds data about the function, length, etc."""
    def __init__(self, min=(-1,-1), max=(1,1), function=lambda x:x, length = 60): 
        self.xmin, self.ymin = min #min and max should be a pair of reals, not an imaginry 
        self.xmax, self.ymax = max
        self.funnction = function
    
    def calculate(self, size=(1920,1080)):
        """calculate the values of the function"""
        print("╔══════════════════════════════")
        print("║  calculating...  ")
        print("║  xmin: " + self.xmin + "; ymin: " + self.ymin)
        print("║  xmax: " + self.xmax + "; ymax: " + self.ymax)
        print("║  function: " + self.function)

        real = np.linspace(self.xmin, self.xmax, size[0])
        complex = np.linspace(self.ymin, self.ymax, size[1])
        plane = np.meshgrid(real, complex)

        print("║  Done!")
        print("╚══════════════════════════════")
        
a = keyframe()