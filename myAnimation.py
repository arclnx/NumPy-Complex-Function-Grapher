import complexAnimation as anim
myanim = anim.animation()
a = anim.keyframe(function ="x", length=60)
b = anim.keyframe(function = "np.sqrt(x)", length=4)
myanim.addKeyframe(a)
myanim.addKeyframe(b)
myanim.render(size=(1440,1440), folderPath="C:\\Users\\trevo\\Desktop\\Grapher_Output")