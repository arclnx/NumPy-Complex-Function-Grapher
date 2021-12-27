import numpy as np

def hsl_to_rgb2(H,S,L):
    """takes H,S,L inputs, where H is [0,360], and S,L are [0,1]"""

    def max2(a,b):
        return np.where(a>b,a,b)

    def min2(a,b):
        return np.where(a<b,a,b)

    def f(n):
        k = (n + H/30)%12
        a = S * min2(L,1-L)
        return L - a * max2(-1,min2(k-3,min2(9-k,1)))

    return (f(0),f(8),f(4))

def ComplexToRGB(complex):
    """takes a complex number and returns a tuple of RGB values in the range [0,1]"""
    angle = ((np.angle(complex,deg=True)+360)%360)/360
    magnitude = np.absolute(complex)
    rawColor =  hsl_to_rgb2(angle,1-np.log2(magnitude)%1,.5)
    return rawColor

print(np.absolute(np.inf+2j))
print(np.log2(np.inf))