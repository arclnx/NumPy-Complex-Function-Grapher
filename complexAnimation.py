import numpy as np

class animation:
    """Create an animation that holds keyframes"""
    def __init__(self, width=1920, height=1080, colorfunc=None):
        self.width, self.height = width, height #resolution of animation in pixels
        self.keyframes = [] #list of all keyframes

class keyframe:
    """create a keyframe that holds data about the function, length, etc."""
    def __init__(self, min=(-1,-1), max=(1,1),function = lambda x:x, length = 60):
        self.xmin, self.ymin = min
        self.xmax, self.ymax = max
    
    def render(self, size=(1920,1080)):
        
        pass