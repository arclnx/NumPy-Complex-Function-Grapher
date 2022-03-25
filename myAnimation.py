import complexAnimation as anim

myanim = anim.animation()
a = anim.keyframe(function = "(x+1j*np.sin(x))/(1j*np.tanh(1/(x+1j)))",  min=(-4,-4), max=(4,4), length=60)
b = anim.keyframe(function = "2**x",                              min=(-8,-8), max=(8,8), length=4)
myanim.addKeyframe(a)
#myanim.addKeyframe(b)

# "(1-x)**(2/(x**2+1j))/((2-x)**2)"

myanim.render(size=(1440,1440), folderPath="C:\\Users\\TAK\\Desktop\\Python\\Grapher_Output\\f(x)=fib(x)")
#myanim.render(size=(1440,1440), folderPath="C:\\Users\\trevo\\Desktop\\Grapher_Output")