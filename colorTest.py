import numpy as np
import colorsys as colorsys
import timeit

def hsl_to_rgb2(H,S,L):
    def max2(a,b):
        return np.where(a>b,a,b)
    
    def min2(a,b):
        return np.where(a<b,a,b)

    def f(n):
        k = (n + H/30)%12
        a = S * min2(L,1-L)
        return L - a * max2(-1,min2(k-3,min2(9-k,1)))
    return (f(0),f(8),f(4))

def ComplexToRGB2(complex):
    angle = ((np.angle(complex,deg=True)+360)%360)/360
    magnitude = np.absolute(complex)
    rawColor =  hsl_to_rgb2(angle,1-np.log2(magnitude)%1,.5)
    return rawColor

real = np.linspace(-1,1,1920)
complex = np.linspace(-1,1,1080)
real, complex = np.meshgrid(real, complex, indexing='ij')
cplane = real + complex*1j

print(cplane)
#print(ComplexToRGB2(foo))
#print(colorsys.hls_to_rgb(.5,.6,1))
print("start")

for i in range(10):
    ComplexToRGB2(cplane)

print("done")