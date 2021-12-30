import complexAnimation as anim
myanim = anim.animation()
a = anim.keyframe(length=10)
b = anim.keyframe(function = "x**2", length=4)
myanim.addKeyframe(a)
myanim.addKeyframe(b)
myanim.render(size=(1080*2,1080*2), folderPath="C:\\Users\\trevo\\Desktop\\Grapher_Output")