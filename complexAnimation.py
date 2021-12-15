import numpy as np

class animation:
    """Create an animation that holds keyframes"""
    def __init__(self, width=1920, height=1080):
        self.width, self.height = width, height
        self.keyframes = []

class keyframe:
    """create a keyframe that holds data about the function, length, etc."""
    def __init__(self, )