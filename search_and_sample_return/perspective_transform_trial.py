import matplotlib.image as mpimg
import matplotlib.pyplot as plt
# Uncomment the next line for use in a Jupyter notebook
# This enables the interactive matplotlib window
#%matplotlib notebook
image = mpimg.imread('example_grid1.jpg')
plt.imshow(image)
plt.show()

## perspective transform points
## clockwise from lower left
# 13.04 139.82
# 118.42 95.73
# 199.28 95.30
# 301.65 139.38