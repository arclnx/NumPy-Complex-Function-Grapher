import complexAnimation as anim

myanim = anim.animation()
a = anim.keyframe(function = "x",          smin=(-8,-8), max=(8,8), length=60)
b = anim.keyframe(function = "(x**2-1)/(x**2+1)", min=(-8,-8), max=(8,8), length=4)
myanim.addKeyframe(a)
myanim.addKeyframe(b)

myanim.render(size=(1440,1440), folderPath="C:\\Users\\TAK\\Desktop\\Python\\Grapher_Output\\f(x)=x to f(x)=(x^2-1) div (x^2+1)")
#myanim.render(size=(1440,1440), folderPath="C:\\Users\\trevo\\Desktop\\Grapher_Output")