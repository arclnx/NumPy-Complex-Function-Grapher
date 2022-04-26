import complexAnimation as anim
import numpy as np

def mosaic(function, pixelSize, min, max, tiledSize, folderPath):
    tiledWidth = tiledSize[0]
    tiledHeight = tiledSize[1]
    tilePixelSize = (pixelSize(0)/tiledWidth,pixelSize(1)/tiledHeight)
    
    # Calculate x and y coordinates by linearly spacing bewteen max and min
    x_coords = np.linspace(min[0],max[0],tiledWidth+1)
    y_coords = np.linspace(min[1],max[1],tiledHeight+1)
    
    # render each image in the grid
    for row in range(tiledHeight):
        for column in range(tiledWidth):
            tile = anim.animation()
            tile.addKeyframe(function=function,
                             min=(x_coords[row], y_coords[column]),
                             max=(x_coords[row+1], y_coords[column+1]),
                             length=1)
            tile.render(size=tilePixelSize, folderPath=folderPath)
            
    