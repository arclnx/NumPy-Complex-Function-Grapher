import complexAnimation as anim

myanim = anim.animation()
a = anim.keyframe(function = "x",                 min=(-8,-8), max=(8,8), length=60)
b = anim.keyframe(function = "e**(np.pi*x)", min=(-8,-8), max=(8,8), length=4)
myanim.addKeyframe(a)
myanim.addKeyframe(b)

myanim.render(size=(1440,1440), folderPath="C:\\Users\\TAK\\Desktop\\Python\\Grapher_Output\\f(x)=x to f(x)=e^(pi*x)")
#myanim.render(size=(1440,1440), folderPath="C:\\Users\\trevo\\Desktop\\Grapher_Output")