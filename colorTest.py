from PIL import Image as im
import numpy as np

def ComplexToRGB(complex):
    phase = np.angle(complex,deg=True)
    