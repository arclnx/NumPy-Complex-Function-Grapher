import numpy as np

def hsl_to_rgb2(H,S,L):
    """takes H,S,L inputs, where H is [0,360], and S,L are [0,1], and returns integer RGB values in the form RGB, R,G,B are [0,255]"""

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
    """takes a complex number and returns a tuple of integer RGB values in the range [0,255]"""
    angle = np.nan_to_num(((np.angle(complex,deg=True)+360)%360))
    magnitude = np.absolute(complex)
    rawColor =  hsl_to_rgb2(angle,1-np.nan_to_num(np.log2(magnitude))%1,.5)
    return rawColor

real = np.linspace(-1,1,10)
complex = np.linspace(-1,1,10)
real, complex = np.meshgrid(real, complex, indexing='ij')
cplane = real + complex*1j
print(ComplexToRGB(cplane))
print("--------")
print(ComplexToRGB(cplane).T)
print(ComplexToRGB(cplane).T.shape)
print(ComplexToRGB(cplane).T[0][0])