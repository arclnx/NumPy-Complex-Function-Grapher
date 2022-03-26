import complexAnimation as anim


myanim = anim.animation()
a = anim.keyframe(function = "(x+1j*np.sin(x))/(1j*np.tanh(1/(x**2j)))",  min=(-4,-4), max=(4,4), length=60)
myanim.addKeyframe(a)


myanim.render(size=(1440*5,1440*5), folderPath="C:\\Users\\TAK\\Desktop\\Python\\Grapher_Output\\f(x)=fib(x)")
#myanim.render(size=(1440,1440), folderPath="C:\\Users\\trevo\\Desktop\\Grapher_Output")