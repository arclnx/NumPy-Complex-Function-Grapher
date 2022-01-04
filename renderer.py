"""
Handles converting complex data arrays into images and saving them, as well as turning series of images to toa video
"""

import color as color
from PIL import Image

def renderFrames(frameData, folderPath, frameNumber):
    """
    Apply the complex->RGB function to a 2d array, then save it as a PNG at the location specified

    Parameters
    ---
    frameData : 2d numpy array of complex numbers
        The complex number data to render
    folderPath : string
        A string that holds a path to the folder to save the images to
    frameNumber : integer
        An integer that is left-padded and used as a file name
        
    Returns
    ---
    Nothing : Saves an image
    """
    # apply the complex->RGB function, then transpose to get the right shape
    renderedFrame = color.ComplexToRGB(frameData)
    
    # convert the np.ndarray to a PIL image
    frameImage = Image.fromarray(renderedFrame.T,"RGB")
    
    # set the filepath
    filePath = folderPath + "\\" + str(frameNumber).rjust(4,"0") + ".png"
    
    # save the image
    frameImage.save(filePath)