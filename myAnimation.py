import complexAnimation as anim

myanim = anim.animation()
a = anim.keyframe(function = "(1-x)**(1/x**2)/((1+x)**2)",                  min=(-4,-4), max=(4,4), length=60)
b = anim.keyframe(function = "2**x", min=(-8,-8), max=(8,8), length=4)
myanim.addKeyframe(a)
#myanim.addKeyframe(b)

myanim.render(size=(1440*4,1440*4), folderPath="C:\\Users\\TAK\\Desktop\\Python\\Grapher_Output\\f(x)=fib(x)")
#myanim.render(size=(1440,1440), folderPath="C:\\Users\\trevo\\Desktop\\Grapher_Output")