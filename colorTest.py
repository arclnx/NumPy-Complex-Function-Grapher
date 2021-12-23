from PIL import Image as im
import numpy as np

def ComplexToRGB1(complex):
    angle = np.angle(complex,deg=True)
    angle = angle if angle<=0 else angle+180
    return angle

def ComplexToRGB2(complex):
    return (np.angle(complex,deg=True)+360)%360