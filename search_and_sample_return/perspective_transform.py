import cv2
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


image = mpimg.imread('example_grid1.jpg')

def perspect_transform(img, src, dst):

    # Get transform matrix using cv2.getPerspectivTransform()
    M = cv2.getPerspectiveTransform(src, dst)
    # Warp image using cv2.warpPerspective()
    # keep same size as input image
    warped = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))
    # Return the result
    return warped

# Define source and destination points

## perspective transform points
## clockwise from lower left
# 13.04 139.82
# 118.42 95.73
# 199.28 95.30
# 301.65 139.38
#source = np.float32([[ 13.04, 139.82 ], [ 118.42, 95.73 ], [ 199.28, 95.30 ], [ 301.65, 139.38 ]])
#destination = np.float32([[ 0, 0 ], [ 0, 10 ], [ 10, 10 ], [ 10, 0 ]])      

dst_size = 5 
# Set a bottom offset to account for the fact that the bottom of the image 
# is not the position of the rover but a bit in front of it
bottom_offset = 6
source = np.float32([[14, 140], [301 ,140],[200, 96], [118, 96]])
destination = np.float32([[image.shape[1]/2 - dst_size, image.shape[0] - bottom_offset],
                  [image.shape[1]/2 + dst_size, image.shape[0] - bottom_offset],
                  [image.shape[1]/2 + dst_size, image.shape[0] - 2*dst_size - bottom_offset], 
                  [image.shape[1]/2 - dst_size, image.shape[0] - 2*dst_size - bottom_offset],
                  ])

warped = perspect_transform(image, source, destination)
plt.imshow(warped)
plt.show()
