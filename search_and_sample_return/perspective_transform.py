import cv2
import numpy as np

def perspect_transform(img, src, dst):

    # Get transform matrix using cv2.getPerspectivTransform()
    M = cv2.getPerspectiveTransform(src, dst)
    # Warp image using cv2.warpPerspective()
    # keep same size as input image
    warped = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))
    # Return the result
    return warped

# Define source and destination points
source = np.float32([[ , ], [ , ], [ , ], [ , ]])
destination = np.float32([[ , ], [ , ], [ , ], [ , ]])      

warped = perspect_transform(image, source, destination)
plt.imshow(warped)
plt.show()
