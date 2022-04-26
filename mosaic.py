import complexAnimation as anim
import numpy as np

def mosaic(function, pixelSize, min, max, tiledSize, folderPath):
    tiledWidth = tiledSize[0]
    tiledHeight = tiledSize[1]
    x_coords = np.linspace(min)