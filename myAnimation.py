import complexAnimation as anim
import mosaic

myanim = anim.animation()
a = anim.keyframe(function = "(x+1j*np.sin(x))/(1j*np.tanh(1/(x**2j)))",  min=(-4,-4), max=(4,4), length=60)
b = anim.keyframe(function = "x", min=(-4,-4), max=(4,4), length = 60)
myanim.addKeyframe(a)
myanim.addKeyframe(b)

myanim.render(size=(1440,1440), folderPath="C:\\Users\\TAK\\Desktop\\Python\\Grapher_Output\\f(x)=fancyfunc")

#mosaic.mosaic(function="(x+1j*np.sin(x))/(1j*np.tanh(1/(x**2j)))",
#              pixelSize=(1920*32, 1080*32),
#              min=(-1,-1080/1920), max=(1,1080/1920),
#              tiledSize=(16,16),
#              folderPath="C:\\Users\\TAK\\Desktop\\Python\\Grapher_Output\\mosaic")