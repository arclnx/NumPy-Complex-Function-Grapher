"""
Handles conversion between complex numbers and HSL and RGB colors
"""

import numpy as np
from numba import jit

def hsl_to_rgb2(H,S,L):
    """
    Convert an HSL color to an RGB one
    
    Parameters
    ---
    H : Real number ∈[0,360]
        The hue of an HSL color
    S : Real number ∈[0,1]
        The saturation of an HSL color
    V : Real number ∈[0,1]
        The value of an HSL color
        
    Returns
    ---
    RGB Color : numpy array
        A 1d array of the RGB compenets of an RGB color, where R,G,B ∈[0,255]
    
    """
    
    def max2(a,b):
        return np.where(a>b,a,b)
    
    def min2(a,b):
        return np.where(a<b,a,b)

    def f(n):
        k = (n + H/30)%12
        a = S * min2(L,1-L)
        return L - a * max2(-1,min2(k-3,min2(9-k,1)))

    return np.array([f(0)*255,f(8)*255,f(4)*255]).astype(np.uint8)

def ComplexToRGB(complex):
    """
    Take a complex number and return an RGB color
    
    Parameters
    ---
    complex : complex number
        A complex number, can have inf or nan components
    
    Returns
    ---
    Color : numpy array
        A 1d array of the RGB compenets of an RGB color, where R,G,B ∈[0,255]
    """
    angle = np.nan_to_num(((np.angle(complex,deg=True)+360)%360))
    magnitude = np.absolute(complex)
    color =  hsl_to_rgb2(angle,
                            1-0.125*(np.nan_to_num(np.log2(magnitude))%1),
                            .5 - 0.125*(np.nan_to_num(np.log2(magnitude))%1))
    return color