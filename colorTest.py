from PIL import Image as im
import numpy as np
import colorsys as color

def ComplexToRGB1(complex):
    angle = np.angle(complex,deg=True)
    angle = angle if angle<=0 else angle+180
    return angle

def ComplexToRGB2(complex):
    angle = ((np.angle(complex,deg=True)+360)%360)/360
    magnitude = np.absolute(complex)
    return color.hls_to_rgb(angle,0.5,1-np.log2(magnitude)%1)

test=np.linspace(-1-1j,1+1j,11)
ComplexToRGB2Vector = np.vectorize(ComplexToRGB2)
print("start")
print(ComplexToRGB2Vector(test))
print("done")