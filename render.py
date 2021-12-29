import color
from PIL import Image

def render(frameData, folderPath, frameNumber):
    # apply the complex->RGB function, then transpose to get the right shape
    renderedFrame = color.ComplexToRGB(frameData)
    
    # convert the np.ndarray to a PIL image
    frameImage = Image.fromarray(renderedFrame.T,"RGB")
    
    # set the filepath
    filePath = folderPath + "\\" + str(frameNumber).rjust(4,"0") + ".png"
    
    # save the image
    frameImage.save(filePath)